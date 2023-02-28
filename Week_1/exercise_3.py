#Take 10 integers from a user and give both sum and average

userInput = input("Enter 10 integers:").split()

userIntegers = []
sum = 0
average = 0

#Converts user input to int from str
for x in userInput:
    userIntegers.append(int(x))

#adds each int to a total sum 
for x in userIntegers:
    sum += x

#calculates the average
average = sum / len(userIntegers)

#prints the results
print("Sum of the integers is: " + str(sum))
print('Average of the integers is: ' + str(average))