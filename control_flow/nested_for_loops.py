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