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

#####################################################
# Nested Loops - Loops inside of loops
#####################################################

# Pretend you are a restaurant program.
# You have a list of people currently waiting for food.
# You want to feed them each food item in the list one at a time.
people = ['John', 'Mary', 'Bob', 'Jane', 'Jack', 'Jill', 'Fyron']
foods = ['Pizza', 'Pasta', 'Salad', 'Sandwich', 'Cake', 'Pie', 'Soup']

# The indention here is important.
for person in people:
    for food in foods:
        print(person, 'is going to eat', food)
    print()

# In other words, each person is a single iteration of the outer loop
# and for that single outer loop iteration, you loop through the foods
# list for however many food items there are in the list.
# If there are 6 people and 4 food items, there will be
# 6 outer loop iterations and 4 inner loop iterations per outer loop iteration.

# The total amount of iterations will be 6 * 4 = 24 iterations.
########################################################

# Another example to calculate the fibonacci sequence
num1 = 0
num2 = 1
print("Fibonacci sequence:")
print(num1)
print(num2)
for i in range(0, 10):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)

# Another example to calculate the factorial of a number
num = 500
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)