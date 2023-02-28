#Program to convert Farenheit to Celsius and vice versa
#Note: The conversion on the sheet was incorrect from C to F, I double checked my conversion online. 

running = True

#Welcome Message

welcomeMessage = """*Temperature Conversion Program*
Enter 1. For Celsius to Fahrenheit
Enter 2. For Fahrenheit to Celsius
Enter 3 to Quit: ___

"""


while running:
    userChoice = input(welcomeMessage)

    #Converts Farenheit to Celcius
    if userChoice == '1':
        userInput = input("Enter Farenheit Temperature: ")
        convertedTemp = (int(userInput) - 32) * 0.5556
        print(userInput + " Farenheit is equivalent to \"" + str(convertedTemp) + "\" Celcius \n")
    
    #Converts Celcius to Farenheit
    elif userChoice == '2':
        userInput = input("Enter Celcius Temperature: ")
        convertedTemp = (int(userInput) * 1.8) + 32
        print(userInput + " Celcius is equivalent to \"" + str(convertedTemp) + "\" Farenheit \n")
    
    #Ends the loop
    elif userChoice == '3':
        running = False

    #If there is an invalid input
    else:
        print(welcomeMessage)