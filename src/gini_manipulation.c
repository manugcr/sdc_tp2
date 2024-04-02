/**
 * @file gini_manipulation.c
 * @brief Gini Library
 * 
 * This library gets a GINI Index FLOAT value from python, converts it to INT 
 * and adds 1 and returns it back to python.
 * 
 * @param gini_index FLOAT
 * @return gini_index INT
*/
int _gini_manipulation(float gini_index) 
{
    int gini_index_int = (int)gini_index;
    return gini_index_int + 1;
}