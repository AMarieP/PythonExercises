# Perform the following operation on the given Binary Tree (s):

# 1. Pre-order Traversing
# 2. In-order Traversing
# 3. Post-order traversing

class BinarySearchNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    #Insert new data into the Binary Tree
    def insert(self, value):
        #If node has NO VALUE then insert the value
        if not self.value:
            self.value = value
            return

        #If value already exists do nothing
        if self.value == value:
            return
        
        #If value is less than node's value AND left child exists call insert on left child
        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            #If a left child does not exist then set the left node to the value
            else:
                self.left = BinaryNode(value)
            return
        
        #If there is a right child then call insert on the right child, else set value to node's right child.
        if self.right:
            self.right.insert(value)
            return
        else:
            self.right = BinaryNode(value)
    
    #Get the min and max values - simple recursive functions that move down the right/left of tree
    def getMinVal(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value
    
    def getMaxVal(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    #TRAVERSING METHODS
    #Pre-Order Traversing
    def preOrder(self, values):
        if self.value is not None:
            values.append(self.value)
        if self.left is not None:
            self.left.preOrder(values)
        if self.right is not None:
            self.right.preOrder(values)
        return values
    
    #In-Order Traversing
    def inOrder(self, values):
        if self.left is not None:
            self.left.inOrder(values)
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            self.right.inOrder(values)
        return values
    
    #Post-Order Traversing
    def postOrder(self, values):
        if self.left is not None:
            self.left.postOrder(values)
        if self.right is not None:
            self.right.postOrder(values)
        if self.value is not None:
            values.append(self.value)
        return values
