
# Challenge
# Make a piece of code that takes a string and validates it by seeing if it has at least one letter and one number
# If the string does not have at least one letter and one number, print "Invalid String"
# If the string has at least one letter and one number, print "Valid String"

password = "1234g56789"
letter_found = False
number_found = False
position = 0

while position < len(password):
    letter = password[position]
    print(letter)
    if letter.isalpha():
        letter_found = True
    if letter.isdigit():
        number_found = True
    position = position + 1

if letter_found and number_found:
    print("Valid Password")
else:
    print("Invalid Password")