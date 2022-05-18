# If Statements - a way to control the flow of your program execution

# if <condition>:
#   <block of code>

# if, elif, else

# If we are hungry, and the food we want is in the list, we can eat it.
foods = ["pizza", "tacos", "sushi", "burritos", "chicken", "steak", "emily sternfield"]
food_wanted = "tacos"
am_hungry = False
can_we_eat = False

if am_hungry and foods.count(food_wanted) > 0:
    can_we_eat = True
    print("Yes, the food you want is in the list and you can eat it.")
else:
    print("You are either not hungry or the food you want is not on the list.")