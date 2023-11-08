import sys

class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.right = self.left = None  # Initially, both left and right children are None
        self.data = data  # Assign data to the Node

class Solution:
    # Function to insert a node with given data in the BST
    def insert(self, root, data):
        if root is None:
            return Node(data)  # Return a new node if root does not exist
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root 

    # Function to perform level-order traversal of the BST
    def levelOrder(self, root):
        queue = []  # Initialize a list to use as a queue
        if root:
            queue.append(root)  # Start with the root node
        
        while queue:
            node = queue.pop(0)  # Pop the first node in the queue
            print(node.data, end=" ") 
            # If the left child exists, add it to the queue
            if node.left:
                queue.append(node.left)
            # If the right child exists, add it to the queue
            if node.right:
                queue.append(node.right)

# Read nodes
T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
# Perform level-order traversal and print the nodes
myTree.levelOrder(root)
