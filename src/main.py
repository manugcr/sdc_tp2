# ------------------------------------------------------------------------------------------------------------------
# File: main.py
# Author:   Gil Cernich, Manuel
#           Pallardo, Agustin
#           Saporito, Franco
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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load the library and define the argument and return types of the C function
libgini = ctypes.CDLL('./include/libgini.so')
libgini._gini_manipulation.argtypes = [ctypes.c_float]
libgini._gini_manipulation.restype = ctypes.c_int


# @brief Manipulates the Gini index from a C function
#
# @paran:
#     num (float): The Gini index value.
# @return:
#     int: The manipulated Gini index value.
def _gini_manipulation(num):
    return libgini._gini_manipulation(num)


# @brief Retrieves the Gini index value for a given country code.
#
# @param:
#     country_code (str): The alpha-3 country code.
# @return:
#     float or None: The Gini index value if available, None otherwise.
def get_gini(country_code):
    try:
        url = f"https://api.worldbank.org/v2/en/country/{country_code}/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
       
        # gini_values = {entry['date']: entry['value'] for entry in data[1] if entry.get('value') is not None}
        gini_values = {entry['date']: _gini_manipulation(float(entry['value'])) for entry in data[1] if entry.get('value') is not None}
       
        return gini_values
    except (requests.RequestException, IndexError, ValueError) as e:
        print(f"Error fetching Gini index for {country_code}: {e}")
        return None


# @brief Calculate the Gini index for the selected countries.
# 
# @param: None
# @returns: None
#
# This function retrieves the Gini index values for each selected country and stores 
# them in the 'gini_dict' dictionary.
# It ensures that at least one country is selected from the listbox and limits the 
# selection to five countries.
def calculate_gini():
    selected_countries = listbox.curselection()
    if not selected_countries:
        messagebox.showwarning("Warning", "Please select at least one country.")
        return

    if len(selected_countries) > 5:
        messagebox.showwarning("Warning", "You can select up to 5 countries.")
        return

    gini_dict.clear()
    for index in selected_countries:
        country = countries[index]
        gini_over_years = get_gini(country['alpha3'])
        if gini_over_years is not None:
            gini_dict[country['name']] = gini_over_years
        else:
            gini_dict[country['name']] = {}

    plot_graph()


# @brief Plot the Gini index values over the years for selected countries.
#
# @param None
# @returns None
#
# This function plots the Gini index values over the years for each selected country.
# It retrieves Gini index data from the 'gini_dict' dictionary and plots them on a single graph.
# The function sets the Y-axis ticks to integer values separated by one.
def plot_graph():
    plt.figure(figsize=(8, 6))
    
    all_sorted_values = []
    
    for country, gini_over_years in gini_dict.items():
        years = list(map(int, gini_over_years.keys()))
        values = list(gini_over_years.values())
        
        try:
            # Sort the years in ascending order
            sorted_years, sorted_values = zip(*sorted(zip(years, values)))
        except ValueError:
            print(f"No data available for {country}")
            continue

        plt.plot(sorted_years, sorted_values, label=country)
        all_sorted_values.extend(sorted_values)
    
    min_value = min(all_sorted_values)
    max_value = max(all_sorted_values)
    
    # Set Y ticks to be integers separated by 1
    plt.yticks(range(int(min_value), int(max_value) + 1, 1))
    plt.xticks(range(min(years), max(years) + 1, 1))
    
    plt.xlabel('Year')
    plt.ylabel('GINI Index')
    plt.title('GINI Index Over Years')
    plt.legend()
    plt.grid(True)

    # Clear previous canvas (if exists)
    if hasattr(root, 'canvas'):
        root.canvas.get_tk_widget().destroy()

    # Create a canvas to embed the plot in the Tkinter GUI
    root.canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    root.canvas.draw()
    root.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    button_calculate.pack(side=tk.BOTTOM, pady=(10, 20)) 


# @brief Create the graphical user interface (GUI) for the GINI index calculator.
#
# @param None
# @returns None
#
# This function creates the GUI window using Tkinter.
# It includes a listbox to display selectable countries, a "Get GINI" button to trigger 
# the calculation, and handles the window close event to ensure proper termination.
def create_gui():
    global listbox, root, button_calculate

    root = tk.Tk()
    root.title("Country GINI Index Calculator")

    # Add margin and padding to the listbox
    listbox_frame = tk.Frame(root, padx=20, pady=20)
    listbox_frame.pack(fill=tk.BOTH, expand=True)  # Fill entire space
    listbox_font = ('Helvetica', 14, 'bold')  # Set the font family and size
    listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, font=listbox_font)  # Apply font to listbox
    for country in countries:
        listbox.insert(tk.END, country['name'])
    listbox.pack(fill=tk.BOTH, expand=True)  # Fill entire space

    # Create a button frame to ensure the button stays visible
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X)
    button_calculate = tk.Button(button_frame, text="Get GINI", command=calculate_gini)
    button_calculate.pack(side=tk.BOTTOM)

    # Bind a function to the window close event to ensure proper termination
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()



# @brief Handle the window closing event.
#
# @param None
# @returns None
#
# This function is called when the user closes the Tkinter window.
# It destroys the Tkinter window, closes all matplotlib figures, and quits the Tkinter main loop, 
# allowing the script to exit gracefully.
def on_closing():
    root.destroy()
    plt.close('all')
    root.quit()


if __name__ == "__main__":
    gini_dict = {}

    # Load country list from JSON file
    # The JSON file contains a list of country names and alpha-3 codes
    with open("./data/countries.json") as json_file:
        countries = json.load(json_file)

    create_gui()
