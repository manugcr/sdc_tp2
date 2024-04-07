import ctypes
import timeit

# Load the shared library
libgini = ctypes.CDLL('./include/libgini.so')
libgini._gini_manipulation.argtypes = [ctypes.c_float]
libgini._gini_manipulation.restype = ctypes.c_int

# Python equivalent of the C function
def gini_manipulation_python(gini_index):
    gini_index_int = int(gini_index)
    return gini_index_int + 1

# Profile the execution time of the C function
time_taken_c = timeit.timeit("libgini._gini_manipulation(42.5)", globals=globals(), number=1000000)

# Profile the execution time of the Python function
time_taken_python = timeit.timeit("gini_manipulation_python(42.5)", globals=globals(), number=1000000)

# Verify outputs of the C function and Python function
# Just to debug and  make sure the outputs are correct
c_output = libgini._gini_manipulation(42.5)
python_output = gini_manipulation_python(42.5)
print("Output of C function:", c_output)
print("Output of Python function:", python_output)
    
print("Time taken by C code:", time_taken_c)
print("Time taken by Python code:", time_taken_python)
