/**
 * @brief Manipulates the Gini index value.
 * 
 * This function calls the assembly function to manipulate the Gini index value.
 * The function receives a Gini index value as a floating-point number from Python,
 * converts it to an integer, increments it by 1, and returns the result back to Python.
 * 
 * @param gini_index The Gini index value as a FLOAT.
 * @return The manipulated Gini index value as an INT.
 */

/* External declaration of the assembly function */
extern int gini_manipulation_asm(float gini_index);

int _gini_manipulation(float gini_index) 
{
    /* Call the assembly function */
    return gini_manipulation_asm(gini_index);
}


// // Pure C code
// int _gini_manipulation(float gini_index) 
// {
//     int gini_index_int = (int)gini_index;
//     return gini_index_int + 1;
// }
