class Node:
    def __init__(self, data):
        # Initialize left and right child nodes as None
        self.right = self.left = None
        # Store the data value of the node
        self.data = data

class Solution:
    # Method to insert a node into a binary search tree
    def insert(self, root, data):
        if root is None:
            # If the tree is empty, create a new node with the given data
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    # Method to calculate the height of a binary tree
    def getHeight(self, root):
        if root is None:
            # Base case: If the tree is empty (root is None), return -1
            return -1
        else:
            # Recursively calculate the height of the left and right subtrees
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            # Return the height of the current node by adding 1 to the maximum
            return 1 + max(leftHeight, rightHeight)

# Main program
T = int(input())  
myTree = Solution()  # Create an instance of the Solution class
root = None  
for i in range(T):
    data = int(input())  # Read data for each node to be inserted
    root = myTree.insert(root, data) 
height = myTree.getHeight(root)  # Calculate the height of the binary tree
print(height)  
