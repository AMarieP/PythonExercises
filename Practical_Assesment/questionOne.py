# QUESTION 1: VALIDATE AN EXPRESSION
# Create a program that will help to validate an expression to see if it has the 
# correct number of matching brackets. 
# It should ask the user to enter an expression to validate, 
# and the type of bracket characters to match.

# Create a function named ExpValidator ( ) that receives two arguments; 
# 1. an expression and 2. a pair of characters to validate the expression.

def ExpValidator(anExpression, charPair):
    validator = []
    #assign names to each charecter to be validated so it is easier to read
    openChar = charPair[0]
    closeChar = charPair[2]
    
    #Loops through the expression to find occurances of the opening/closing chars
    for x in anExpression:
        if x == openChar:
            validator.append(x)
        elif x == closeChar:
            if validator == []:
                return "Invalid Expression"
            else:
                validator.pop()
    
    #Checks if the validator is empty at the end of the string or not and returns our answer
    if len(validator) == 0:
        return "Valid Expression"
    else:
        return "Invalid Expression"

# Within the program, prompt user to input the expression and pair of characters to 
# validate the expression, i.e. ( and ), [ and ], { and }, < and >.
    
running = True

print("Welcome to the expression validating program.")
expression = input('Enter your expression: ')
charToVal = ((input('Enter the opening and closing characters to validate in the format "character AND character:" ')).split())
print(charToVal)
print(ExpValidator(expression, charToVal))

#Loop which runs while running is True prompting the user to continue or end the prgram
#after the first expression has been validated
while running == True:    
    tryAgain = input('Do you want to try again? (Y/N): ')
    if tryAgain == 'N' or tryAgain == 'n':
        print('Bye Bye!')
        running = False
    elif tryAgain == 'Y' or tryAgain == 'y':
        expression = input('Enter your expression: ')
        charToVal = ((input('Enter the opening and closing characters to validate: ')).split())
        print(charToVal)
        print(ExpValidator(expression, charToVal))
    else:
        print('Please choose Y or N!')
    

