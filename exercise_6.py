# Write a Python program that prints the table from 1 to 12. 
# Each row should display 4 tables with proper format. 

timesTableFormat = "{0} x {1} = {2}"
allTables = []
i = 1
holder = "hi"

#Function to make times table with an inputted multipule and return the array
def makeTableData(x):
    y = 1
    table = []
    while y < 11:
        output = x * y
        table.append(timesTableFormat.format(holder,y, output))
        y += 1
    return table

#All Tables needed in allTables array
while i <= 12:
   allTables.append(makeTableData(i))
   i += 1


for x in allTables:
    print('''{:^10} 
{:^10} 
{:^10} 
{:^10}
{:^10} 
{:^10} 
{:^10}
{:^10} 
{:^10} 
{:^10}'''.format(*x))

# print('''{:^10} 
# {:^10} 
# {:^10} 
# {:^10}
# {:^10} 
# {:^10} 
# {:^10}
# {:^10} 
# {:^10} 
# {:^10}'''.format(*allTables[1]))


# def printTable(table):
#     for x in table:


