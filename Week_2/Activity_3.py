# Write a Python program to convert a list of multiple integers into a single integer.

sampleList = [11, 33, 50]

def singleInteger(list):
    singleInteger = ''
    for x in list:
        singleInteger += str(x)
    return int(singleInteger)

print(singleInteger(sampleList))