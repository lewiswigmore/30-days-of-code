# Initialize an empty dictionary 'd' to store name and phone number pairs.
d = {}

# Read the number of entries from the user.
n = int(input())

# Populate the dictionary 'd' with name and phone number entries.
for i in range(n):
    entry = input().split(" ")
    d[entry[0]] = entry[1]

# Continuously read names and look up their corresponding phone numbers.
while True:
    try:
        name = input()
    except EOFError:
        break  # Exit the loop if there is no more input.

    # Check if the 'name' exists in the dictionary 'd'.
    if name in d:
        # If found, print the name and its corresponding phone number.
        print(name, d.get(name), sep="=")
    else:
        # If not found, print "Not found."
        print("Not found")
