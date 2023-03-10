# Write Python Program that contains a Linked List and perform the following 
# operations on it. You can store any random values to the LinkedList.

# Insert a new node at the beginning. 
# Insert a new node at the end. 
# Insert a new node at the middle. 
# Remove first node. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    #Checks if there is a head Node, if none creates a head, 
    # if head node exists append the chain
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
            nodesList.append("End of List")
            return " -> ".join(nodesList)

    #Sets the next node of the newNode to the current head, sets head to newNode
    def insertAtBeginning(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    #Iterates through each node until the end and then sets the next node
    #after the last node to the newNode value
    def insertAtTheEnd(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode:
                prevNode = currentNode
                currentNode = currentNode.next
            prevNode.next = newNode
    
    #Iterates through each node until it finds the specified node to delete
    #Sets the previous node's next to the node after the deleteNode
    #sets deleteNode to none
    def deleteMiddleNode(self, deleteNode):
        if self.head == None:
            raise Exception("No nodes to remove")
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.data == deleteNode:
                    break
                prevNode = currentNode
                currentNode = currentNode.next
            prevNode.next = currentNode.next
            currentNode = None

    #Sets the head to the next node after the original self.head
    def removeFirstNode(self):
        if self.head == None:
            raise Exception("No nodes to remove")
        else:
            firstNode = self.head
            self.head = firstNode.next


testList = LinkedList(['a', 'b', 'c', 'd', 1 , 2 , 3])
print("Create my Linked List: \n" + str(testList) + "\n")

testList.insertAtBeginning(Node('beginning'))
print("Add 'beginning' to the start of my Linked List: \n" + str(testList) + "\n")

testList.insertAtTheEnd(Node('end'))
print("Add 'end' to the end of my Linked List: \n" + str(testList) + "\n")

testList.deleteMiddleNode('d')
print("Delete node 'd' from my Linked List: \n" + str(testList) + "\n")

testList.removeFirstNode()
print("Remove the first node from my Linked List: \n" + str(testList) + "\n")