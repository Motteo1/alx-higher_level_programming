### Python - Classes & Objects
>Each file holds code that illustrates the concepts of classes, instances, private/public fields/attributes, methods/functions, `__str__` to print, comparator methods (`!=` `__ne__`,`==` `__eq__` `>=` `__ge__` `>` `__gt__` `<` `__ly__` `<=`)

#### Description
0. create empty square class and build on this class in the next files
1. Add privat attribute size
2. define size is int and >= 0 else TypeError
3. Define public method area with ValueError if size < 0
4. Access and update private attribute
5. Print a square based on the previous files
6. define private postion attribute to use in printing offsets
7. 100 - create head, insert nodes, ptint with `__str__`
8. 101 - define `__str__` method to print square if called with print()
9. 102 - define comparator methods
10. 103 - recreate code to match the following Bytecode:
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```

### Environment
* Language: Pyhton 3.4.3
* OS: Ubuntu 20.04 LTS
* Compiler: python3
* Stype guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) || [Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

***

### Authors
[Motteo1](https://github.com/Motteo1)
