# Functions
# A function is a named group of code.

# The two main benefits of functions are:
# 1. Code Reuse - The code does not have to be completely rewritten every time we want to use it.
# 2. Modularity - A piece of code that has a specific meaning or task is broken up into its own function.

# Defining a function:
def function_name():
    print("Hello World")

# Calling a function:
function_name()

# In a previous video, we made a chunk of code that
# prints the factorial of a number.
# Every time you want to use that code, you have to copy
# and paste it. That's a lot of typing. And is wack.

# Here is where a function comes in.
def calculate_factorial():
    num = 500
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of", num, "is", factorial)

# Now, when we want to calculate the factorial of a number,
# we "call" the function. This has the effect of running the
# code in the function.
calculate_factorial()

# We can also call the function multiple times.
calculate_factorial()
calculate_factorial()
calculate_factorial()

# Here is a function that will print my name in a box.
def print_name():
    print("##########")
    print("# Kody Simpson #")
    print("##########")

print_name()

# Here is a function that will add two numbers and print the result.
def add():
    num1 = 5
    num2 = 6
    print("Adding", num1, "and", num2)
    print("Result:", num1 + num2)

add()

# There is one downside to the add function we created above.
# The numbers that we are adding are hard-coded into the function.
# If there was a way to "pass in" numbers
# we could dynamically add any two numbers. That's where parameters come in.