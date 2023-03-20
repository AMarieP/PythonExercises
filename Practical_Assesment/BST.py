# QUESTION 3: BINARY SEARCH TREE
# Write a Python program that constructs a Binary Search Tree from given user input,
#  and perform traversing operations.

#Node class which creates the Nodes of the tree
class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    #Assigns data to nodes
    def Insert(self, value):
        #If node has NO VALUE then insert the value
        if not self.value:
            self.value = value
            return

        #If value already exists do nothing no duplicates
        if self.value == value:
            return
        
        #If value is less than node's value AND left child exists call insert on left child
        if value < self.value:
            if self.left:
                self.left.Insert(value)
                return
            #If a left child does not exist then set the left node to the value
            else:
                self.left = Node(value)
            return
        
        #If there is a right child then call insert on the right child, else set value to node's right child.
        if self.right:
            self.right.Insert(value)
            return
        else:
            self.right = Node(value)
    
    #Function which prints tree
    def PrintTree(self):
        if self.value:
            print(self.value)
            if self.left:
                self.left.PrintTree()
            if self.right:
                self.right.PrintTree()
    
    #Preorder Traversal of tree
    def PreOrderTraversal(self, preOrder):
        if self.value is not None:
            preOrder.append(self.value)
        if self.left is not None:
            self.left.PreOrderTraversal(preOrder)
        if self.right is not None:
            self.right.PreOrderTraversal(preOrder)
        return preOrder


def Main():
    running = True
    
    #Inner Function to convert a string to int in array
    def StringToInt(stringArray):
        intArray = []
        for x in stringArray:
            y = int(x)
            intArray.append(y)
        return intArray
    
    #Inner function to convert data to nodes
    def DataToNode(myData):
        myBST = Node(myData[0])
        myData.pop(0)
        for x in myData:
            myBST.Insert(x)
        return myBST

    print("Welcome to the Binary Search Tree.")
    while running:
        data = str(input("Enter data to construct a binary search tree:")).split()
        data = StringToInt(data)
        binaryTree = DataToNode(data)
        print(f"The Pre Order Traversal of the Binary Tree is: {binaryTree.PreOrderTraversal([])}")
        cont = input("Do you wish to try again? (Y/N)?")
        if cont == 'N' or cont == 'n':
            running = False

Main()