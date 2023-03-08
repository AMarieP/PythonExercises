# A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.

# •	Think of five programming words you’ve learned about in previous courses. 

# •	Use these words as the keys in your glossary, and store their meanings as values.

# •	Print each word and its meaning as neatly formatted output. 

# •	You might print the word followed by a colon and then its meaning,
#  or print the word on one line and then print its meaning indented on a second line.
#  
# •	Use the newline character (\n) to insert a blank line between
#  each word-meaning pair in your output.

programmingDict = {
    "Loop" : "A statement to process the same instructions again and again until it is told to stop.",
    "Variable" : "A container for storing data values.",
    "Boolean" : "Boolean is a data type which can be either True or False.",
    "Integer" : "Number type variable which is a whole number of unlimited length (in Python)",
    "Class" : "An object constructor."
}

for x in programmingDict:
    print(x + ":\n" + programmingDict[x] + '\n')