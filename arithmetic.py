# Basic math operations
print(2 + 2)  # addition
print(2 - 2)  # subtraction
print(2 * 2)  # multiplication
print(2 / 2)  # division
print(2 ** 2)  # exponent
print(2 % 2)  # modulus(remainder)
print(2 // 2)  # floor division

# Nuances of division
print(5 / 2)  # 2.5
# When you do division, you get a float back no matter what.
print(4 / 2)  # 2.0

# When you do floor division, you get a number with no decimal places.
print(5 // 2)  # 2
print(5.0 // 2)  # 2.0

# Nuances all together
# Whenever at least one of the operands is a float, the result will be a float.

# Python also supports Order of Operations(PEMDAS), something you probably learned in school.
# PEMDAS is the order in which operations are performed.
# Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

# You don't really need to rememeber that in detail,
# just know really that parenthesis are used to group operations.

# Demonstration of Order of Operations
print(3 + 2 * 2)  # 7, not 10(multiplication is performed over addition)
print((3 + 2) * 2)  # 10 (parenthesis are used to group operations)
print(3 + 2 * 2 + 1)  # 8
print(3 + (2 * 2) + 1)  # 7

# Where can I use this math? Any place that takes a number as an argument. (like print)
# You can also of course use it in a variable.
awesome_variable = 3 + 2 * 2  # 7
print(awesome_variable)
awesome_variable = awesome_variable * 2  # 14
print(awesome_variable)

# There are also shortcuts for doing math on a variable.
counter = 0
counter += 1  # counter = counter + 1
print(counter)  # 1
counter -= 1  # counter = counter - 1
print(counter)  # 0

counter += 2  # counter = counter + 2
print(counter)  # 2
counter *= 2  # counter = counter * 2
print(counter)  # 4
