## Default Arguments and Keyword Arguments in Python functions

# Default Arguments -
# Arguments that are assigned a default value in the function definition.
# If no value is passed for the argument at the time of calling the function, the default value is used.

def greet(name, msg="Good morning!"):
    print("Hello", name + ', ' + msg)

greet("Bruce", "Wassup man?")
greet("Billy Bob")

# In Python, default arguments must be specified after all
# of the required (non-default) arguments in the function definition.

# Illegal:
# def greet(msg="Good morning!", name):
#     print("Hello", name + ', ' + msg)

# Keyword Arguments:
# Traditionally, arguments in a function are passed as a fixed position,
# i.e. the first argument in the function definition is the first argument.
# These are called positional arguments.

# Keyword arguments allow you to specify the argument name with the value
# so that the arguments can be passed in any order.

def simple_greet(name, greeting):
    print("Hey", name + ', ' + greeting)


simple_greet(name="Bruce", greeting="Wassup")
simple_greet(greeting="Wassup", name="Bruce")

# A cool, advanced example of default arguments and keyword arguments:
def calculate_bmi(weight, height, unit="kg", round_to=2):
    if unit == "kg":
        bmi = weight / (height ** 2)
    elif unit == "lb":
        bmi = (weight / (height ** 2)) * 703
    return round(bmi, round_to)

bmi = calculate_bmi(70, 1.75) # using the default unit and round_to values
bmi = calculate_bmi(weight=155, height=5.5, unit="lb", round_to=3)
bmi = calculate_bmi(155, 5.5, round_to=3)
bmi = calculate_bmi(155, 5.5, "lb")