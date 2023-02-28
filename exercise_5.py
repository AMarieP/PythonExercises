#Write a program in Python to display the multiplication table of a given integer

userInput = int(input("Enter an Integer number (Table to be calculated): "))
table = "{0} x {1} = {2}"
output = 0 
x = 1


while x < 11:
    output = x * userInput
    print(table.format(userInput, x, output))
    x += 1