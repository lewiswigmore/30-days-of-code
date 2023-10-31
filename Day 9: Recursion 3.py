import os

# Define a function to compute the factorial using iteration.
def iterativeFactorial(n):
    # Initialize the factorial result to 1.
    f = 1
    # Use a for loop to calculate the factorial.
    for i in range(1, n + 1):
        f = f * i
    return f

# Define a function to compute the factorial using recursion.
def factorial(n):
    # Base case: if n is less than 2, return 1.
    if n < 2:
        return 1
    else:
        # Recursive case: return n multiplied by the factorial of (n-1).
        return n * factorial(n - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
