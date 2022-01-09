# Strings - a data-type that holds characters(letters, numbers, symbols, etc)

# strings are something we have already been using a bit, for our print function
print("I am printing a string of characters")
print('I am also printing a string of characters, except using single quotes to represent the string')

name = "Kody"
name = 'Kody'

# As you can see above, you can use double or single quotes for strings.
# But, you may choose one over another if you have a quote in your string.

quote = 'Abraham Lincoln once said, "Let there be light!"'
another_example = "I don't really understand how people don't like tacos"

# Changing the case of Strings using Methods(functions)
# calling these functions on your strings will run some code behind the scenes and then
# give back a new modified string that you can use. Here, we print it out.
print(name.upper())
print(name.lower())
print(name.title())

# You don't have to print the result, you can store it in the variable
print("Current name: ")
print(name)
name = name.upper()
print("Modified name: ")
print(name)

# String formatting(f-strings) - putting variables in your strings to create a new string
# simply put an f before the quotes and Python will know to do formatting wherever you have
# curly brackets with a variable in between.
my_age = 20
introduction = f"Hello, my name is {name} and I am {my_age} years old."
print(introduction)

# It doesn't have to be a variable between the brackets, but really any value that you want
# to be formatted into the string
print(f"1 + 1 = {1 + 1}")

# Whitespace in Strings and Escape Sequences
# whitespace is any character that is not visible such as spaces, tabs, etc
# When you have a backslash, that is called escaping. \t or \n is an escape sequence.
print("Here is a tab:   .")
print("Here is a tab:\t.")

# The newline character - Creating multiple lines in strings
story = "Once upon a time,\nThere was a little Daniel.\nAnd he didn't know about SimpAPI.\n\t\tThe end."
print(story)

# Functions to remove whitespace
clean_me_up = "      roosevelt 2020.      "
print(clean_me_up)
print(clean_me_up.lstrip())
print(clean_me_up.rstrip())
print(clean_me_up.strip())