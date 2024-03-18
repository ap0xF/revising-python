import logging

# MULTILINE STRINGS, GIVES RAW output or what you see is 
# what you get.

str = """this
        is
    a line
    using multiline
    feature of python
    which can be used by
    sorrounding string with 
    triple quotes"""

print(str)

# long statements can be broken down
# into multiple lines

if (1 < 2) and (2 < 4) and (4 < 8) and (8 < 16) and (16 < 32) and (32 < 64) \
        and (64 < 128) and (128 < 256):
    print(True)

# Casing
# variables, functions, methods and modules are written in snake_case
# classes are written in PascalCase -- just like in java
# constants are written in CAPATALIZED_SNAKE_CASE
