S = input()

# Try to convert the input string to an integer
try:
    # Attempt to convert 'S' to an integer and print it
    print(int(S))
except ValueError:
    # If a ValueError occurs, this code block is executed
    print("Bad String")
