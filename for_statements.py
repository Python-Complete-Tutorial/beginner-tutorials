# For Statements/For Loops
# A way of looping through stuff

victims = ['John', 'Mary', 'Bob', 'Jane']

# Loop through each element in the list and print it out
# with all the letters capitalized.
for victim in victims:
    print(victim.upper())

# Pretty lit right? Each time a single "iteration" of the loop has run,
# the victim variable will be assigned to the next element in the list.

# Loop through the list backwards
for victim in reversed(victims):
    print(victim.upper())
    print("died by eating too much cheese.")

# Another random example to calculate the sum of all the numbers in a list
totalSum = 0
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    totalSum += number
print("Sum of all the numbers: ", totalSum)

# In other languages, for loops are usually made with a number that
# represents the number of times the loop should run. This does not
# have to be the case, but it is common to have an index variable
# associated with the for statement.

# A similar way of looping based on an arbitrary number can be done
# with the range function inside the for statement.
# Range will return a list of numbers from 0 to 1 less than the number given.
for i in range(5): # loop 5 times and print the number
    print(i)

# Loop through the same list of victims but using a range of numbers
# that represents each index in the list.
for i in range(len(victims)):
    print(victims[i])

#####################################################
# Continue and Break Statements
#####################################################

# Continue = skip the current iteration and continue with the next
# Break = Completely break out of the loop

# Example
# This will have the effect of printing 0, 1, 2, and 4
# but skipping the tree because we checked and continued.
for i in range(5):
    if i == 3:
        continue
    print(i)

# This will break out of the loop after printing 0, 1, 2
for i in range(5):
    if i == 3:
        break
    print(i)