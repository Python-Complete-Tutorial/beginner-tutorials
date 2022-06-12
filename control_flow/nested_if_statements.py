# Nested If Statements - if statements inside of if statements

# Sometimes it becomes necessary to have more directions for your program to take after making a decision already.

# Example of nesting:
if True:
    if True:
        print("Cows are cool")
    else:
        print("Cows are not cool")

# They work the exact same way, the indentation is still
# important to indicate that the code is part of the if statement.
speed = 10000 # miles per hour
turn_needed = False

if turn_needed:
    print("The car needs to turn")
    if speed > 15:
        print("The car is going too fact, slowing down.")
    else:
        print("...Turning...")
else:
    print("I dont need to turn yet")