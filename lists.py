# Lists in Python
# A way to store multiple values in a single variable
# a "collection" of values

# This here is a list of strings, 4 strings essentially in 1 variable name
my_favorite_names = ["Randy", "Billy", "Bob", "Billy Bob"]
random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Here is a list of mixed data types, not commonly seen in other major languages such as Java, C++, etc.
mixed_types = ["Randy", 1, "Billy", 2, "Bob", 3, "Billy Bob", 4, 5, 6, 7, 8, 9, 10]

# Sometimes, you may want a list and then to fill it with values later
# empty list.
empty_list = []

# If you want to visually see the data in your list, you can still use the print function
print(my_favorite_names)
print(random_numbers)
print(mixed_types)
print(empty_list)

# Basic List Operations

# If you want to get a specific value from a list, you can use the index number.
# The index number starts at 0, so the first value in the list is at index 0. (zero-based)
print(my_favorite_names[0])  # Randy
print(my_favorite_names[1])  # Billy
print(my_favorite_names[2])  # Bob

# You can also use negative numbers to get values from the end of the list.
# The last value in the list is at index -1.
print(my_favorite_names[-1])  # Billy Bob
print(my_favorite_names[-2])  # Bob

# If you put an invalid index number in, you will get an error.
# print(my_favorite_names[-5]) # IndexError: list index out of range

# You can add values to a list by using the append function
empty_list.append("Randy")
empty_list.append("Billy")
empty_list.append("Bob")
print(empty_list)  # ["Randy", "Billy", "Bob"], the list is now filled with 3 values

# You can also use the insert function to add values at a specific index
empty_list = []  # reset the list by reasigning it to an empty list
empty_list.insert(0, "Randy")
empty_list.insert(1, "Billy")
empty_list.insert(2, "Bob")
print(empty_list)  # ["Randy", "Billy", "Bob"]

# If you insert into the middle of a list, the values after the index will shift over.
empty_list.insert(1, "Billy Bob")
print(empty_list)  # ["Randy", "Billy Bob", "Billy", "Bob"]

# You can also use the remove function to remove a value from a list
empty_list.remove("Billy Bob")
print(empty_list)  # ["Randy", "Billy", "Bob"]

# You can also use the pop function to remove a value from the end of the list or at a specific index
empty_list.pop()
print(empty_list)  # ["Randy", "Billy"]
empty_list.pop(1)
print(empty_list)  # ["Randy"]

# You can also use the clear function to clear the list, removing all values
empty_list.clear()
print(empty_list)  # []

# using the extend function to add multiple values to a list
empty_list.extend(["Randy", "Billy", "Bob"])
print(empty_list)  # ["Randy", "Billy", "Bob"]