if __name__ == '__main__':
    # Read an integer 'n' from the user's input.
    n = int(input().strip())
    
    # Read a list of integers 'arr' from user input and split it into individual integers.
    arr = list(map(int, input().rstrip().split()))
    
    # Reverse the list 'arr' and store it in 'r'.
    r = arr[::-1]
    
    # Iterate through the reversed list 'r' and print each element with a space at the end.
    for i in r:
        print(i, end=" ")
