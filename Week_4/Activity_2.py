# Write a Python program to count the number of digits in a number using recursion.
#Assumes input is greater than 0

sampleNumbers = int(input("Input any Number:"))

def CountNumbers(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return CountNumbers(num // 10) + 1


print(CountNumbers(sampleNumbers))