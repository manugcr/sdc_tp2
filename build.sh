#!/bin/bash

if [ -d "./build" ]; then
    echo "  -> Removing old build directory."
    rm -rf ./build/*
else
    echo "  -> Creating build directory."
    mkdir ./build
fi

if [ -d "./include" ]; then
    echo "  -> Removing old build directory."
    rm -rf ./include/*
else
    echo "  -> Creating build directory."
    mkdir ./include
fi

echo "  -> Compiling the C code into an object file."
gcc -c -Wall -Werror -fpic ./src/gini_manipulation.c -o ./build/gini_manipulation_c.o

echo "  -> Compiling the object file into a shared library" 
gcc -shared -W -o ./include/libgini.so ./build/gini_manipulation_c.o

echo "  -> Compilation successful lib at ./include/"
