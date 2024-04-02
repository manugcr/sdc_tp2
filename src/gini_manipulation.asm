global _gini_manipulation_asm

section .text
_gini_manipulation_asm:
    ; Convert float to int
    fld dword [esp + 4]     ; Load float from stack
    fistp dword [esp + 4]   ; Store integer part back to stack

    ; Add 1 to the integer
    mov eax, dword [esp + 4]  ; Load integer from stack
    add eax, 1                ; Add 1
    mov dword [esp + 4], eax  ; Store the result back to stack

    ret
