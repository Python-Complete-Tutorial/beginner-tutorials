## Modules

# Modules can be thought of as a bundle of code, in this case a way of
# grouping like functions together.

# Benefits of modules:
# 1. Code Reuse - We can utilize a bunch of pre-written code without having to write it ourselves every time.
# 2. Modularity - A piece of code that has a specific meaning or task is broken up into its own module.
# 3. Abstraction - A module can be thought of as a black box. We don't need to know how it works,
#    we just need to know how to use the functions it provides.

# The math module is a module that contains a bunch of math functions.
# We can import the math module and use the functions in it.

## Importing a module:
import math  # This imports the math module and allows you to use any function in it.
from math import pow  # This imports the pow function from the math module.
from math import *  # This imports all of the functions in the math module.

## Calling a function from a module:
print(math.pow(2, 3)) # Calculates 2^3

# When you import a specific function(or *) from a module, you can call it directly.
print(pow(2, 3)) # Calculates 2^3

# You can also import a module and give it a nickname.
import math as m
print(m.pow(2, 3)) # Calculates 2^3

# You can also give a module function a nickname.
from math import pow as p
print(p(2, 3)) # Calculates 2^3

## How to Create a Module
# Modules are just Python files with a .py extension.
# The name of the module is the name of the file.
# Simple as that.

# I made a module called kitchen.py for you to look at.
