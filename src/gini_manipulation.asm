section .text
    global gini_manipulation_asm    ; Declare the function as global

gini_manipulation_asm:
    ; Start 
    push ebp                        ; Save the value of the base pointer
    mov ebp, esp                    ; Set the base pointer to the current stack pointer position

    ; Convert float to int
    fld dword [ebp+8]               ; Load the float argument from the stack into the FPU register
    fistp dword [ebp-4]             ; Store the integer result at ebp-4

    ; Add 1 to the integer
    mov eax, dword [ebp-4]          ; Move the integer result to the EAX register
    add eax, 1                      ; Add 1 to the integer in the EAX register

    ; Exit
    mov esp, ebp                    ; Restore the stack pointer to the base pointer value
    pop ebp                         ; Restore the base pointer
    ret                             ; Return from the function, with the result in the EAX register
