# If Statements - A way to control the flow of your programs execution

# Anatomy of an if statement
# if <condition>:
#   <block of code>

# The condition of an if statement depends on somethin that is evaluated to a boolean value
# Last episode helps here.

# Let's make a simple program that decides whether we can enter the bar or not
age = 20
drinking_age = 21

if age >= drinking_age:
    print("You can enter the bar")

# This gives your program a more dynamic nature. Your program can run code
# differently depending on the values of your variables and the conditions being met.
# AWESOME.

# You can also chain together multiple if statements to give your program
# multiple paths that it can take.
drinks_drank_count = 455
if drinks_drank_count < 99:
    print("Please drink more. You have not drank enough.")
elif 100 <= drinks_drank_count < 500:
    print("You are about to become tipsy. Slow down partner.")
elif drinks_drank_count >= 500:
    print("You are drunk. You should not be drinking. Please stop. Please.")

# An else branch can be added if you want some code to run if none of the other
# conditions/branches are met.
favorite_color = "navy blue"
if favorite_color == "navy blue":
    print("You have a nice favorite color.")
elif favorite_color == "blood red":
    print("You good bro?")
else:
    print("You have poor taste.")


# If we are hungry, and the food we want is in the list, we can eat it.
foods = ["pizza", "tacos", "sushi", "burritos", "chicken", "steak", "emily sternfield"]
can_we_eat = False
food_wanted = "tacos"
am_hungry = True

if am_hungry and foods.count(food_wanted) > 0:
    can_we_eat = True

print(f"Can we eat {food_wanted}? {can_we_eat}")
