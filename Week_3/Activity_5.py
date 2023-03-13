# Write a Python program and create a LinkedList and perform the following tasks.
# You can store any random values in the LinkedList.

# 1. Find the maximum value from a double-ended linked list.

# 2. Insert a new node at the beginning of a double-ended Linked List.

# 3. Insert a new node at the end of a double-ended Linked List.

# 4. Insert a new node at the middle of a double-ended Linked List.

# 5. Remove first node of a double-ended Linked List.

# 6. Remove last node of a double-ended Linked List.

# 7. Remove middle node of a double-ended Linked List.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data

class LinkedListDeque:

    def __init__(self, nodes = None):
        self.head = self.rear = None
        if nodes != None:
            node = Node(data = nodes.pop(0))
            self.head = node
            node.prev = None
            for x in nodes:
                node.next = Node(data = x)
                prevNode = node
                node = node.next
                node.prev = prevNode
                if node.next == None:
                    self.rear = node

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

    def maxValue(self):
        maxVal = 0
        currentNode = self.head
        while currentNode:
            if currentNode.data > maxVal:
                maxVal = currentNode.data
            currentNode = currentNode.next
        return maxVal

    def insertAtBeginning(self, newNodeData):
        newNode = Node(newNodeData)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, newNodeData):
        newNode = Node(newNodeData)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = None
            newNode.prev = self.rear
            self.rear = newNode

    def insertAtMiddle(self, newNodeData):
        newNode = Node(newNodeData)
        pass

testList = LinkedListDeque([1, 3, 4, 5])
testList.insertAtEnd(8)
print(testList.rear.data)