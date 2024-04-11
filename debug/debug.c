#include <stdio.h>

extern int gini_manipulation_asm(float gini_index);

int main(int argc, char argv[]) 
{
    float gini_index = 42.3;
    int result;

    /* Call the assembly function */
    result = gini_manipulation_asm(gini_index);

    printf("%f -> %d\n", gini_index, result);

    return 0;
}
