# There are different types of data that a variable can store. These are known
# as data-types. In this program we take a look at number types and how we
# can store different types of numbers in variables.

# Integers - whole numbers that can be generally any size you need
my_age = 20
how_much_i_love_tacos = 100000000000000000000000000000000000000000000000000000

print(my_age)
print(how_much_i_love_tacos)

# negative numbers can be stored too, it is still known as an integer
negative_number = -999
print(negative_number)

# Floats - numbers that have decimal points
# obviously in the real world you won't always use whole numbers(integers)
# so for things like calculations you can store 'floats' in variables
pi = 3.14
more_precise = 3.1415926535897932384626433832795028841971

print(pi)
# floats do have limits to their size so when you print this variable holding a float
# out, you will see it is cut off at a certain point. For most programs the precision
# or the amount of decimal places that can be stored is enough.
print(more_precise)

# There will be a seperate tutorial on arithmatic with Python, but just know you
# can perform math on your variables if you want.
pi = 3.14
radius = 30 # meters
area_of_circle = pi * (radius * radius) # area = pi*r^2
print("The area of my circle is: ")
print(area_of_circle)

# Different ways of representing integers and floats

# Sometimes big numbers can get hard to read. Try representing 21 billion(option1).
# if you didnt write this code it might take you a sec to read it with your brain.
# To rememedy this, Python allows you to put underscores in your numbers(option2) so that
# they essentially act as commas that would appear as you write numbers in real life.
option1 = 21000000000
option2 = 21_000_000_000

# Exponential Notation for Floats
# obviously very important for representing big and small numbers, this can be
# done in Python
electric_constant = 8.85e-12 # 8.85 * 10^-12
yo_mommas_mass = 56.73e69 # 56.73 * 10^69