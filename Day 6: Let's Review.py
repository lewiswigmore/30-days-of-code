# Read an integer input from STDIN.
x = int(input())

# Loop through a range of 0 to x (exclusive).
for i in range(0, x):
    # Read a string input from STDIN.
    s = input()
    
    # Print the modified string, combining characters at even and odd indices with a space.
    print(str(s[0::2] + " " + s[1::2]))
