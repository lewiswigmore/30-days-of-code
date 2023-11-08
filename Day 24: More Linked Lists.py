class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Insert a new node with 'data' into the linked list 'head'.
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    # Display the linked list starting from 'head'.
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()  # Print a newline to separate the output.

    # Remove duplicate elements from the linked list.
    def removeDuplicates(self, head):
        current = head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next  # Skip the duplicate node.
            else:
                current = current.next  # Move to the next node.
        return head

mylist = Solution()
T = int(input("Enter the number of elements: "))
head = None
for i in range(T):
    data = int(input("Enter element {}: ".format(i + 1)))
    head = mylist.insert(head, data)

head = mylist.removeDuplicates(head)
print("Linked list after removing duplicates:")
mylist.display(head)
