# This is a module called kitchen. It contains functions that a kitchen might need.

# This is a function that will print a recipe.
def print_recipe(recipe):
    print("Recipe:")
    for ingredient in recipe:
        print(ingredient)

# This is a function that will cook a recipe.
def cook_recipe(recipe):
    print("Cooking recipe:")
    for ingredient in recipe:
        print(ingredient)

def measure_liquid(liquid):
    print("Measuring", liquid)
