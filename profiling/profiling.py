import ctypes
import timeit

# Load the C shared library
libginiC = ctypes.CDLL('./include/libgini_c.so')
libginiC._gini_manipulation.argtypes = [ctypes.c_float]
libginiC._gini_manipulation.restype = ctypes.c_int

# Load the C-ASM shared library
libginiASM = ctypes.CDLL('./include/libgini_asm.so')
libginiASM._gini_manipulation.argtypes = [ctypes.c_float]
libginiASM._gini_manipulation.restype = ctypes.c_int

# Python equivalent of the C function
def gini_manipulation_python(gini_index):
    gini_index_int = int(gini_index)
    return gini_index_int + 1

# Profile the execution time of the C function
time_taken_c = timeit.timeit("libginiC._gini_manipulation(42.3)", globals=globals(), number=1000000)

# Profile the execution time of the C-ASM function
time_taken_asm = timeit.timeit("libginiASM._gini_manipulation(42.3)", globals=globals(), number=1000000)

# Profile the execution time of the Python function
time_taken_python = timeit.timeit("gini_manipulation_python(42.3)", globals=globals(), number=1000000)

# Verify outputs of the C, C+ASM and Python function
# Just to debug and  make sure the outputs are correct
c_output = libginiC._gini_manipulation(42.3)
asm_output = libginiASM._gini_manipulation(42.3)
python_output = gini_manipulation_python(42.3)
print("Output of C+ASM function:", asm_output)
print("Output of C function:", c_output)
print("Output of Python function:", python_output)
    
print("Time taken by C+asm code:", time_taken_asm)
print("Time taken by C code:", time_taken_c)
print("Time taken by Python code:", time_taken_python)
