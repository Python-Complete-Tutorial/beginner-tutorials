# Comparison Operators - == != < > <= >=
# These are used to compare values and produce a boolean result
# They are most useful for conditions(coming soon)

# Important note: == is different from =
# == is used to compare the value of two variables
# = is used to assign a value to a variable

# They are all pretty self explanatory, String types
# though are compared based on lexicographical(alphabetical) order.
# I will cover that in a later section.
print(True == True)         # True
print(True == False)        # False
print(69 == 45)             # False
print("obama" == "cheese")  # False

print(True != True)         # False
print(True != False)        # True
print(69 != 45)             # True
print("obama" != "cheese")  # True

print("obama" > "cheese")    # False
print("obama" < "cheese")    # True
print(45 < 69)               # True
print(45 > 69)               # False
print(45 <= 69)              # True
print(45 >= 69)              # False
print([1, 2, 3] < [1, 2, 4]) # True
print([1, 2, 3] > [1, 2, 4]) # False

# Combination of Comparison and Logical Operators
# You can combine comparison and logical operators to make more complex boolean expressions
age = 20
am_i_old = (age >= 18) and (age <= 65) # two comparisons tied together
am_i_really_old = age >= 65

print(am_i_old)

# In Python you can combine comparisons in cool ways that cannot be done in other languages
# Example:
print(1 < 2 < 3) # cannot be done in other languages
print(1 < 2 and 2 < 3) # can be done in other languages