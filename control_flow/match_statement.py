# Match Statement - Also known as switch-case statement
# Another way of branching code, like an if statement does.
# Available only in Python 3.10 and above.

# Rather being based on a condition per se, the match statement is based on a value.
brain_size = "smfall"

# The variable after match is the value that will be compared to the cases.
match brain_size:
    case "small":   # if the variable has the value "small", it will run this code.
        print("You have a small brain")
    case "medium":
        print("You have a medium brain")
    case "large":
        print("You have a large brain")
    case _:                               # This is the default case
        print("You have a huge brain")

http_error = 404
match http_error:
    case 404:
        print("Page not found")
    case 403:
        print("Access denied")
    case 401:
        print("You are not authorized")
    case _:  # not needed
        print("Unknown error")

# If there is no default case and no match is found, a "no-op" occurs.
#  This is a no-op because it does nothing.

# Combining cases:
test_score = 90
match test_score:
    case 90:
        print("You got an A")
    case 80 | 75 | 70:  # the | signifies a logical OR, so if the value is 80, or 75, or 70, it will run this code.
        print("You did okay")
    case 60:
        print("You did poorly")
    case _:
        print("You failed and you are going to die")