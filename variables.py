# Variables - names that hold data in your program

# creating a variable
my_age = 20
# printing out our age
print(my_age)

# variables can hold many "data-types" such as strings
my_name = "Kody Simpson"
print(my_name)

pi = 3.14
print(pi)

# variable reassignment - changing the value that a variable holds after it has been created
my_favorite_quote = "Good things come to bad people."
print("My favorite quote is: ")
print(my_favorite_quote)

# here it is being reassigned to "I like trains."
my_favorite_quote = "I like trains."
print("I changed my favorite quote: ")
print(my_favorite_quote)

# Variable Naming Rules:
# 1. They must only be made of letters, numbers, or underscores
# 2. They can only start with a letter or an underscore, not a number
# 3. Variable names are "case-sensitive"

# valid names:
kodysimpson = "he really likes candy canes"
_kody = 20
xxKody69Simpsonxx = "weird variable name!"

# invalid names:
123iliketacos
kody simpson # there cannot be spaces

# Variable Naming Conventions
# Naming Conventions are rules that most developers follow, but
# are not required by the Python language.
# Regular variables that we will be creating and using in our programs should be named using
# "snake case". This means that the words in the variables are seperated by underscores.
# It helps improve readability for yourself and other people who you share your code with.
this_is_snake_case = "Sssss....."
# again, it is not required. But it is recommended.

# Case-sensitive means that if for example one variable is all lowercase
# and another is uppercase, they are different variables
bob = 123
BOB = 321

# multiple assignment - creating multiple variables at once
a, b, c = 1, 2, 3