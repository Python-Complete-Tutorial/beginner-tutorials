# Boolean Logic and Conditionals

# Booleans in Python - "bool"
# A boolean is true or false.
is_cake_good = False
is_cheesecake_good = True

# negation of a boolean value - flipping it
is_cake_good = not is_cheesecake_good

# bools in Python are numbers behind the scenes
# 1 = True
# 0 = False
boolean_math = True + True + False
print(boolean_math)

# 2/3 = 0.66
another_math = (True + True) / (True + True + True)
print(another_math)

lie = True / True

# Boolean Logical Operators
# Logical operators are a way to combine boolean values into boolean expressions.
# They evaluate to True or False.

# Operators: AND, OR, NOT, XOR
# NOT has already been used in the previous example, simple negation to flip a bool value

# and - if both sides are true, it returns true
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# or - if either side is true, it returns true
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

# xor - if ONLY one side is true, it returns true
print(True ^ True)   # False
print(True ^ False)  # True
print(False ^ True)  # True
print(False ^ False) # False

# not - flips a bool value
print(not True)   # False
print(not False)  # True