# Write a Python program to print even or odd numbers in a given range using recursion.

rangeStart = int(input("WHat is your start range: "))
rangeStop = int(input("What is your stop range: "))

userRange = list(range(rangeStart, rangeStop))

def Loop(sample, evens=None, odds=None):
    if evens is None:
        evens = []
    if odds is None:
        odds = []
    if len(sample) == 0:
        return evens, odds
    else:
        x = sample.pop()
        if x % 2 == 0:
            evens.append(x)
        if x % 2 > 0:
            odds.append(x)
        return Loop(sample, evens, odds)

result = Loop(userRange)

print(f"""All even numbers from {rangeStart} to {rangeStop} are: 
{result[0]}

All odd numbers from {rangeStart} to {rangeStop} are:
{result[1]}""")