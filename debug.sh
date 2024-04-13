echo "  -> Compile the C file"
gcc -m32 -g -c -o ./build/debug.o debug/debug.c

echo "  -> Compile the assembly file"
nasm -f elf32 -o ./build/debug_asm.o src/gini_manipulation.asm

echo "  -> Link the object files together"
gcc -m32 -g -o ./debug/debug ./build/debug.o ./build/debug_asm.o

echo "  -> Get the asm code"
gcc -m32 -S -o ./debug/debug.asm ./debug/debug.c
