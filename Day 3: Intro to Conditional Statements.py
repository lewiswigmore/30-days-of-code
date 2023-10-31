
if __name__ == '__main__':
    # Read an integer 'n' from the user's input
    n = int(input().strip())

    # Check if 'n' is odd
    if n % 2 == 1:
        print("Weird")
    # If 'n' is even, further check its value
    elif n % 2 == 0:
        # If 'n' is between 2 and 5 (inclusive), it's 'Not Weird'
        if 2 <= n <= 5:
            print("Not Weird")
        # If 'n' is between 6 and 20 (inclusive), it's 'Weird'
        if 6 <= n <= 20:
            print("Weird")
        # If 'n' is greater than 20, it's 'Not Weird'
        if n > 20:
            print("Not Weird")
