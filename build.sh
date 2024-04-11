#!/bin/bash

if [ -d "./build" ]; then
    echo "  -> Removing old build directory."
    rm -rf ./build/*
else
    echo "  -> Creating build directory."
    mkdir ./build
fi

if [ -d "./include" ]; then
    echo "  -> Removing old include directory."
    rm -rf ./include/*
else
    echo "  -> Creating include directory."
    mkdir ./include
fi

echo "  -> Compiling the C code into an object file."
gcc -c -m32 -Wall -Werror -fpic ./src/gini_manipulation.c -o ./build/gini_manipulation_c.o

echo "  -> Assemble the asm file into and object file."
nasm -f elf32 ./src/gini_manipulation_asm.asm -o ./build/gini_manipulation_asm.o

echo "  -> Link both object files into a shared library."
gcc -m32 -shared -o ./include/libgini.so ./build/gini_manipulation_c.o ./build/gini_manipulation_asm.o

echo "  -> Compilation successful lib at ./include/"
echo "      -> Execute script with launch.sh"
