#!/bin/bash

if [ -d "./build" ]; then
    echo "  -> Removing old build directory."
    rm -rf ./build/*
else
    echo "  -> Creating build directory."
    mkdir ./build
fi

# echo "  -> Compiling Pure C libary."
# echo "      -> Compiling the C code into an object file."
# gcc -c -m32 -Wall -Werror -fpic ./src/gini_manipulation.c -o ./build/gini_manipulation_c.o
# echo "      -> Compiling the object file into a shared library" 
# gcc -m32 -shared -W -o ./include/libgini_c.so ./build/gini_manipulation_c.o

echo "  -> Compiling C with NASM library."
echo "      -> Compiling the C code into an object file."
gcc -c -m32 -Wall -Werror -fpic ./src/gini_manipulation.c -o ./build/gini_manipulation_c.o
echo "      -> Assemble the asm file into and object file."
nasm -f elf32 ./src/gini_manipulation.asm -o ./build/gini_manipulation_asm.o
echo "      -> Link both object files into a shared library."
gcc -m32 -shared -o ./include/libgini_asm.so ./build/gini_manipulation_c.o ./build/gini_manipulation_asm.o


echo "  -> Compilation successful lib at ./include/"
echo "      -> Execute script with launch.sh"
