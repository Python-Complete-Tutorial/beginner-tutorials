## Passing Lists as Arguments to a Function

# A list can be passed as an argument to a function.
# When we pass a list as an argument, a reference to the list is passed to the function.
# In plain English, this means that any changes made to the list inside the function
# will affect the list outside the function as well.

# Example:
def add_numbers_to_list(numbers):
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)


my_list = [4, 5, 6]
add_numbers_to_list(my_list)
print(my_list)  # [4, 5, 6, 1, 2, 3]


# This does not happen with integers, strings, booleans, etc.
def double_number(number):
    number *= 2


my_number = 5
double_number(my_number)
print(my_number)  # 5

## Making the list a copy so that the original list is not modified
names = ["Bruce", "Billy Bob", "Billy Bob Jr.", "Bobby", "Bobby Jr."]


def add_prefix_to_names(strings):
    for i in range(len(strings)):
        strings[i] = "Mr. " + strings[i]


# Pass the copy of the list to the function
add_prefix_to_names(names[:])  # [:] creates a copy of the list
# The original list is not modified
print(names)
