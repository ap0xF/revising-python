"""
Namespace is like container that holds various types of funcn, methods and objects

Types of namespaces in py -
1. Built-in - always available when python interpreter is running in memory
2. Global
3. Enclosing and Local
"""

# listing everything that falls inside builtin namespace
print(dir(__builtins__))

# checking the module, where the objects listed inside built-in namespace
# are from

print(__builtins__.tuple.__module__)



