# ------------------------------------------------------------------------------------------------------------------
# File: obtain_gini.py
# Author:   NAME
#           NAME
#           NAME
# Date: 2024-04-08
# Description:  This scripts fetches the GINI index of selected countries and provides a GUI to display the data.
#               Once the GINI index is obtained a C function is called from this python script to make some data 
#               processing with assembly and the final value is returned to the GUI.
#
# Data sources: 
# - World Bank API: https://api.worldbank.org/v2/en/
# - Countries JSON: https://github.com/stefangabos/world_countries/tree/master
# ------------------------------------------------------------------------------------------------------------------

import json
import requests
import ctypes
import tkinter as tk
from tkinter import messagebox

# Load the library and define the argument and return types of the C function
libgini = ctypes.CDLL('./include/libgini.so')
libgini._gini_manipulation.argtypes = [ctypes.c_float]
libgini._gini_manipulation.restype = ctypes.c_int


# Manipulates the Gini index from a C function
#
# Args:
#     num (float): The Gini index value.
# Returns:
#     int: The manipulated Gini index value.
def _gini_manipulation(num):
    return libgini._gini_manipulation(num)


# Retrieves the Gini index value for a given country code.
#
# Args:
#     country_code (str): The alpha-3 country code.
# Returns:
#     float or None: The Gini index value if available, None otherwise.
def get_gini(country_code):
    try:
        url = f"https://api.worldbank.org/v2/en/country/{country_code}/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        gini_values = [entry['value'] for entry in data[1] if entry.get('value') is not None]
        return gini_values[0] if gini_values else None
    except (requests.RequestException, IndexError, ValueError) as e:
        print(f"Error fetching Gini index for {country_code}: {e}")
        return None


# Calculate the Gini index for the selected countries.
# The index is manipulated using the wrapped C function before adding it to the dictionary.
# Then it gets displayed in the GUI.
#
# Args:
#     None
# Returns:
#     None
def calculate_gini():
    selected_countries = listbox.curselection()
    if not selected_countries:
        messagebox.showwarning("Warning", "Please select at least one country.")
        return

    if len(selected_countries) > 5:
        messagebox.showwarning("Warning", "You can select up to 5 countries.")
        return

    # Clear the result_label GUI by updating it with an empty string
    result_label.config(text="")
    gini_dict.clear()

    for index in selected_countries:
        country = countries[index]
        gini = get_gini(country['alpha3'])
        if gini is not None:
            # Directly manipulate the gini value before adding it to the dictionary
            gini = _gini_manipulation(float(gini))
            gini_dict[country['name']] = gini
        else:
            gini_dict[country['name']] = "N/A"

    # Update the result label with country names and numeric Gini coefficients
    result_label.config(text="")
    formatted_gini_info = "\n".join(f"{country}: {gini}" for country, gini in gini_dict.items())
    result_label.config(text=formatted_gini_info)


def create_gui():
    global listbox, result_label

    root = tk.Tk()
    root.title("Country GINI Index Calculator")

    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
    for country in countries:
        listbox.insert(tk.END, country['name'])
    listbox.pack()

    result_label = tk.Label(root, text="", font=("Helvetica", 12))
    result_label.pack()

    button_calculate = tk.Button(root, text="Get GINI Indices", command=calculate_gini)
    button_calculate.pack()

    root.mainloop()


if __name__ == "__main__":
    gini_dict = {}

    # Load country list from JSON file
    # The JSON file contains a list of country names and alpha-3 codes
    with open("./data/countries.json") as json_file:
        countries = json.load(json_file)

    create_gui()
