class Solution:
    def __init__(self):
        # Initialize an empty stack and queue
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        # Push a character onto the stack
        self.stack.append(char)

    def enqueueCharacter(self, char):
        # Enqueue a character into the queue
        self.queue.append(char)

    def popCharacter(self):
        # Pop and return the top character from the stack
        return self.stack.pop()

    def dequeueCharacter(self):
        # Dequeue and return the first character from the queue
        return self.queue.pop(0)

# Read the input string
s = input()

# Create a Solution class object
obj = Solution()

# Push/enqueue all the characters of the input string s to stack and queue
for char in s:
    obj.pushCharacter(char)
    obj.enqueueCharacter(char)

isPalindrome = True

# Pop the top character from the stack and dequeue the first character from the queue
# Compare both the characters to check for a palindrome
for _ in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# Print whether the input string s is a palindrome or not
if isPalindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
