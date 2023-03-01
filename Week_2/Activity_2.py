# Write a Python program to count the number of strings where the string length 
# is 2 or more and the first and last character are same from a given list of
# strings. 

#List of strings
sampleList = ['abc', 'xyz', 'aba', '1221']

#Funtion which checks each entry in list for length & if first and last char match
def stringCounter(List):
    validCount = 0
    for x in List:
        if len(x) >= 2 and x[0] == x[len(x) - 1]:
            validCount += 1
    return validCount

validStrings = stringCounter(sampleList)

print('Expected Result: ' + str(validStrings))