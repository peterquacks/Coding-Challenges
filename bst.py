#! python3

# Binary Search Tree

class Node:
    # Constructor
    def __init__(self, val):
        self.value      = val
        self.leftChild  = None
        self.rightChild = None

    def insert(self, data):
        # Check for duplicates
        if self.value == data:
            return False
        
        # Check if data is smaller than current node, check to see if left child exists
        # inserts as left child, if left child doesn't exist, create a new node and assign it as a left child
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    
    # Find function, recursively calls find with either left child when data is less than root, and right if greater than until value is equal
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if left.Child:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if right.Child:
                return self.rightChild.find(data)
            else:
                return False

    # If left child, then print value of the current node, then traverses through left child
    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    # Almost the same as the preorder code but prints it at the end. This allows it to traverse through the tree before printing, giving you the bottom most node every time.
    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    # Now the print statement is in the middle which will print out the left branches first. This will get the bottom most left, then that parent, then the right child of that parent.
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        # If root node doesn't exist create one
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()
        
    def postorder(self):
        print("PostOrder")
        self.root.postorder()
        
    def inorder(self):
        print("InOrder")
        self.root.inorder()




bst = Tree()
bst.insert(10)
print(bst.insert(15))
print(bst.insert(2))
print(bst.insert(35))
print(bst.insert(11))
print(bst.insert(1))
print(bst.insert(5))
print(bst.insert(25))
print(bst.insert(23))
print(bst.insert(17))
print(bst.insert(15))

bst.preorder()
bst.postorder()
bst.inorder()