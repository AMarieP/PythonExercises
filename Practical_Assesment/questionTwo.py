# QUESTION 2: TICKETING SYSTEM
# Create a Python program that simulates queueing in a shop. 
# Customers are seen in the order of their arrival to the shop. 
# The shop operates as per the following conditions:

# A new customer arrives to the shop every 3 seconds.
# The sales assistant could see the next customer every 5 seconds.
# You will need to research on the Python timer function to schedule 
# the repeating tasks stated above.

#DATA STRUCTURE ANALYSIS:
# Why did you select that specific data structure?
#     I selected a list because I am most familiar with lists, an I knew I could use
    # the pop and inset methods to remove from the back/ add to the front effectively making a Queue.

# How was that data structure suited to the task?
#     List methods made it easy to create a FIFO queue which I needed for the ticket system
    # to work as intended. Lists are mutuable which was needed, as we moved down the queue data
    # would be added and removed.

# Could another structre be suited to the task?
#     Dictionary with key:value pairs could be used - especially if I wanted the ticket to
    # contain more information than just the number. The no duplicate condition is desierable
    # as I only want one of each ticket made. The key names would be 'TicketOne' or something 
    # similar so accessing each value may be more intuitive.
    # A set could also be used as no duplicates but changable however accessing items would
    # be less inuitive and more tedious as sets are unordered so I couldn't simply call from the end of the queue
    # I would probably need to set up a counter checking which ticket number we were going to attend next.
    # Finally, I could have made a linked list to make a FILO queue. I think this is the best
    # alternative solution as it can be faster to access each value but I wanted to use a list.
    # The dictionary and set can both be used but I definitely would do a linked list if I have to choose
    # to do this again a diiferent way.

#Program starts below

#Imports
import time  

#My Queue
class Queue:
    def __init__(self):
        self.data = []
        self.ticketCount = 0 #Count of how many tickets total

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    #Returns the queue
    def ShowQueue(self):
       return f'The customers with the following tickets are in the queue: {self.data}'
    
    #Adds a ticket to the queue
    def NewCustomer(self):
        self.ticketCount += 1
        (self.data).insert(0, self.ticketCount)
        return f"Customer with ticket {self.ticketCount} is added to the queue."
    
    #Removes a customer from the front of the queue once attended to
    def SeeCustomers(self):
        if self.isEmpty() == True:
            return "There was no Customer to be attended.\n"
        else:
            seenTicket = self.data.pop()
            return f"The customer with ticket number {seenTicket} will be seen now."

#Variables
myQueue = Queue()
running = True

#Call each function on a timed loop so they will call every 3 and 5 seconds, respectively.

#I decided to do it in a loop like this as if I did two seperate timed functions 'time.sleep' would make 
#the programs actual times out of whack as the program would sleep for 3 sec, then 5 etc and I found threading
#a bit too complex for the application.
def Main():
    print("""*** Welcome to my SHOP ***
      ヾ(＾-＾)ノ

Press Ctrl + C to close the Shop.
""")
    secondsPassed = 0
    while running:
        time.sleep(1)
        secondsPassed += 1
        if secondsPassed % 3 == False:
            print(f"{myQueue.NewCustomer()}\n")
        if secondsPassed % 5 == False:
            print(f"Sales Assistant is ready to see the next customer.\n{myQueue.SeeCustomers()}\n{myQueue.ShowQueue()}\n")


#Makes a nice goodbye message rather than the default.
try:
    Main()
except KeyboardInterrupt:
    print ('Shop Closed! Goodbye --\(￣O￣)')
