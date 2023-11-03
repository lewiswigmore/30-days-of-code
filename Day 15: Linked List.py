class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        # Method to display the linked list
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Method to insert a new node with data at the end of the linked list
        new_node = Node(data)  # Create a new node with the given data
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next  # Traverse to the end of the list
        current.next = new_node  # Add the new node at the end of the list
        return head

mylist = Solution()

T = int(input())  # Number of test cases
head = None

for i in range(T):
    data = int(input())  # Input data
    head = mylist.insert(head, data)  # Insert data into the linked list

mylist.display(head)
