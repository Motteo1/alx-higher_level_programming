# Python - if/else,loops & functions
	each file contains code that illustrates an essential concept of python: if/elif/else loops, range, ord(), chr(), modulo, copy of string, bytecode, etc

*NB. All files are python scripts except #13*

0. Print whether the random number is positive or negative
1. Print the last digit of the number stored in prints the alphabet, in lowercase, not followed by a new line variable
2. Prints the alphabet in lowercase, not followed by a new line
3. Print the alphabets in lowercase, not followed by a new line
4. Prints all numbers from 0 to 98 in decimal and in hexadecimal
5. Prints numbers 0 to 99
6. Prints all possible different combinations of two digits
7. Function that checks for lowercase character
8. Function that prints a string in uppercase  followed by a new line
9. Function that prints the last digit of a number
10. function that computes a to the power of b and returns the value
11. Function that prints the numbers form 1 to 100 separated by a space - FizzBuzz
12. Function in c that inserts a number into a sorted singly linked list
13. Prints the alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase), not followed by anew line
14. Function that creates a copy of the string, removing the character at the position n(not the Python way, the "C array index")
15. Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:

  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16


  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE


  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36


  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE


  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE

# Environmet
 ~ Language: Python 3.4.3 (and C for #13)
 ~ OS: Ubuntu 14.04 LTS
 ~ Compiler: python3 (and gcc 4.8.4)
 ~ Style guidelines: PEP 8 (version 1.7) Betty style

# Authors
 Tim Irungu
