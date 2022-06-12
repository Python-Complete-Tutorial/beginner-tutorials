# Functions
# A function is a named group of a code.

# In a previous video, we made a chunk of code that
# prints the factorial of a number.
# Every time you want to use that code, you have to copy
# and paste it. That's a lot of typing. And is wack.

# Here is where a function comes in.
def fibonacci():
    num = 500
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of", num, "is", factorial)

# Now, when we want to calculate the factorial of a number,
# we "call" the function. This has the effect of running the
# code in the function.
fibonacci()

# There is one downside to the fibonacci function we created above.
# The number that we are calculating the factorial of is
# hard-coded into the function. If there was a way to
# "pass in" a number, we could dynamically calculate the
# factorial of any number.

# Let's rewrite the function to take in a number.
def fibonacci(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of", num, "is", factorial)

# Now, we call the function but as we are calling it
# we also give it a number as its "argument".
fibonacci(5)
fibonacci(700)
fibonacci(69)

# BOOM! Really cool right? We can now calculate the factorial of any number and print it out.
# The two main benefits of functions are:
# 1. Code Reuse - The code does not have to be completely rewritten every time we want to use it.
# 2. Modularity - A piece of code that has a specific meaning or task is broken up into its own function.

# More random functions
def add(num1, num2):
    print("Adding", num1, "and", num2)
    print("Result:", num1 + num2)

add(5, 6)