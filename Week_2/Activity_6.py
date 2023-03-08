# Write a Python program and perform the following operations.
# •	Create a set. 
# •	Iterate over set.
# •	Find maximum and the minimum value in a set. 
# •	Find the length of a set. 
# •	Check if a given value is present in a set or not.  


userInput = set(input("Enter set data seperated by a space: ").split())
running = True

welcomeMessage = '''
Press 1 to iterate over the set
Press 2 to find the Maximum Value
Press 3 to find the Minimum Value
Press 4 to find the Length of the set
Press 5 to check for if a Value is in the set
Press 6 to Exit
'''

def iterateSet(userSet):
    for x in userSet:
        print(x)

myMax = max(userInput)

myMin = min(userInput)

def findLength(userSet):
    length = 0
    for x in userSet:
        length += 1
    return length

def checkForValue(userSet, value):
    valueAppears = 0
    for x in userSet:
        if x == str(value):
            valueAppears += 1
    if valueAppears == True:
        return("The value is present " + str(valueAppears) + " times in the set.")
    else:
        return("The value does not appear in the set")


while running == True:
    chooseFunction = int(input(welcomeMessage))
    if chooseFunction == 1:
        print("\n Your Set:")
        iterateSet(userInput)
    elif chooseFunction == 2:
        print("\n Your maximum is: " + myMax + "\n")
    elif chooseFunction == 3:
        print("\n Your minimum is: " + myMin + "\n")
    elif chooseFunction == 4:
        print("\nYour set length is: " + str(findLength(userInput)) + "\n")
    elif chooseFunction == 5:
        userValue = input("\nWhat value do you want to check?: ")
        print(checkForValue(userInput, userValue))
    elif chooseFunction == 6:
        running = False
    else:
        print("Please enter a valid option\n")