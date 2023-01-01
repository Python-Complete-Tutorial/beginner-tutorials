#################################################
# Functions that "return" values
#################################################

# As you might have noticed, the functions that we used from Python
# can sometimes give a value back. This is called a "return" value.
# We can use the return value to do something else.

# Last tutorial, we wrote a function that adds two numbers and prints
# the result. But what if we wanted to use the result of the addition
# in another part of our code? Let's rewrite the function to return
# the result instead of printing it.

# Original Function
# def add(num1, num2):
#     print("Adding", num1, "and", num2)
#     print("Result:", num1 + num2)

# Rewritten Function
def add(num1, num2):
    print("Adding", num1, "and", num2)
    return num1 + num2


# Now, when we call the function, we can store the result in a variable
# and use it later.
result = add(5, 6)
print("Sum of 5 and 6 is", result)


# We can also use the return value in other functions.
def multiply(num1, num2):
    return num1 * num2

# We can use the result of the add function as an argument to the multiply function.
result = multiply(add(5, 6), 2)
print("5 + 6 * 2 =", result)  # 5 + 6 * 2 = 22

# We can also use the return value in an if statement.
if add(5, 6) == 11:
    print("5 + 6 is 11")
else:
    print("5 + 6 is not 11")

# Returning in different ways:
def exists_in_list(list, needle):
    for item in list:
        if item == needle:
            return True
    return False

# What happens if we don't include that ending return statement? It returns None.
# None is a special value in Python that means "nothing".
# It is similar to null in other languages.