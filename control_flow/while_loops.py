# While Loops - A way to repeat code while a condition is true

# Skeleton of a while loop
# while condition:
#   code to run

# Infinite loop
# while True:
#     print("Hello World!")

# It is important to put a condition in while loop
# that will eventually become false or at least manually break out at some point
number = 21
while number != 0:
    print("This is the number: ", number)
    number = number - 1

# A way of iterating through a list with a while loop
im_hungry = ["Steak", "Chicken", "Fish", "Pizza", "Pasta", "Salad", "Sandwich", "Cake", "Pie", "Soup"]
while im_hungry:  # the condition is true until the list is empty
    food = im_hungry.pop()
    print("I am hungry and I want to eat", food)

# The else statement can also be used with while loops
# to run some code when the condition becomes false
number = 21
while number != 0:
    print("This is the number: ", number)
    number = number - 1
else:
    print("The number is now 0")

# Challenge
# Make a piece of code that takes a string and validates it by seeing if it has at least one letter and one number
# If the string does not have at least one letter and one number, print "Invalid String"
# If the string has at least one letter and one number, print "Valid String"
letter_found = False
number_found = False

position = 0
password = "12345g6789"
while position < len(password):
    letter = password[position]
    # print(letter)
    if letter.isalpha():
        letter_found = True
    if letter.isdigit():
        number_found = True
    position = position + 1

if letter_found and number_found:
    print("Valid String")
else:
    print("Invalid String")
