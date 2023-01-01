# There is one downside to the fibonacci function we created previously.
# The number that we are calculating the factorial of is
# hard-coded into the function. If there was a way to
# "pass in" a number, we could dynamically calculate the
# factorial of any number.

# Let's rewrite the function to take in a number as input.
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of", num, "is", factorial)

# Now, we call the function but as we are calling it
# we also give it a number as its "argument".
calculate_factorial(5)
calculate_factorial(700)
calculate_factorial(69)

# BOOM! Really cool right? We can now calculate the factorial of any number and print it out.

# More random functions
def add(num1, num2):
    print("Adding", num1, "and", num2)
    print("Result:", num1 + num2)

add(5, 6)