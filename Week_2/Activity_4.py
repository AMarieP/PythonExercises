# Write a Python program to print the value 20. The given tuple is a nested tuple.

sampleTuple = ("Orange", [10, 20, 30], (5, 15, 25))

def tupleCheck(tup, value):
    for x in tup:
        for y in x:
            if y == value:
                return value

print(tupleCheck(sampleTuple, 20))