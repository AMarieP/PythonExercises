#Write a Python program that takes distance and time as input
# and displays the speed in, meters per second, kilometres per hour,
# and miles per 


#Request User Input
meters = int(input('Input distance (meters): '))
hours = int(input('Input time (hour): '))
mins = int(input('Input time(minutes): '))
secs = int(input('Input time(seconds): '))

#Other values needed
totalSeconds = (hours * 3600) + (mins * 60) + secs
totalHours = hours + (mins / 60) + (secs / 3600)
kilometers = meters / 1000
miles = kilometers * 0.62137

#Conversions
meterPerSecond = round((meters / totalSeconds), 5)
kilometersPerHour = round((kilometers / totalHours), 5)
milesPerHour = round((miles / totalHours), 5)

#Conversion Output
output = """\nYour speed in meters/sec is {0}
Your speed in km/h is {1}
Your speed in miles/h is {2}
"""
print(output.format(meterPerSecond, kilometersPerHour, milesPerHour))