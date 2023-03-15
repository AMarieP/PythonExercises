# QUESTION 2: TICKETING SYSTEM
# Create a Python program that simulates queueing in a shop. 
# Customers are seen in the order of their arrival to the shop. 
# The shop operates as per the following conditions:

# A new customer arrives to the shop every 3 seconds.
# The sales assistant could see the next customer every 5 seconds.
# You will need to research on the Python timer function to schedule 
# the repeating tasks stated above.

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
def TimedLoop():
    secondsPassed = 0
    while running:
        time.sleep(1)
        secondsPassed += 1
        if secondsPassed % 3 == False:
            print(f"{myQueue.NewCustomer()}\n")
        if secondsPassed % 5 == False:
            print(f"Sales Assistant is ready to see the next customer.\n{myQueue.SeeCustomers()}\n{myQueue.ShowQueue()}\n")



print("""*** Welcome to my SHOP ***
      ヾ(＾-＾)ノ

Press Ctrl + C to close the Shop.
""")

#Makes a nice goodbye message rather than the default.
try:
    TimedLoop()
except KeyboardInterrupt:
    print ('Shop Closed! Goodbye --\(￣O￣)')
