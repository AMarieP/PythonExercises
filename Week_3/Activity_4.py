#Write a Python program to create LinkedList that ask user input and
# display user values in forward and reverse order. 

#Classes for linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes != None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for x in nodes:
                node.next = Node(data = x)
                node = node.next

    def __repr__(self):
        currentNode = self.head
        nodesList = []
        if currentNode == None:
            return "There is no Data"
        else:
            while currentNode:
                nodesList.append(str(currentNode.data))
                currentNode = currentNode.next
            nodesList.append("End of Nodes")
            return " -> ".join(nodesList)

    def reverseDataOrder(self):
        currentNode = self.head
        prevNode = None
        nextNode = None
        if currentNode == None:
            return "There is no Data"
        else:
            while currentNode:
                nextNode = currentNode.next
                currentNode.next = prevNode
                prevNode = currentNode
                currentNode = nextNode
            self.head = prevNode
    
    def printData(self):
        currentNode = self.head
        if currentNode == None:
            return "There is no Data"
        else:
            while currentNode:
                print('Data = ' + currentNode.data)
                currentNode = currentNode.next


#Function for getting user data
def askUserInput(y):
    x = 1
    userDatas = []
    while y:
        userData = input('Input data for node ' + str(x) + ': ' )
        userDatas.append(userData)
        x += 1
        y -= 1
    return userDatas


nodesAmount = int(input('Input the Number of Nodes: '))
userList = LinkedList(askUserInput(nodesAmount))

print('\nThe list in forward order is:')
userList.printData()

print('\nThe list in backwards order is:')
userList.reverseDataOrder()
userList.printData()
