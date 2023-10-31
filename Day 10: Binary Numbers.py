if __name__ == '__main':
    n = int(input().strip())
    
    # Convert the decimal number to a binary string and remove the '0b' prefix
    b = bin(n)[2:]
    
    # Convert the binary string to a list of characters
    lst = list(b)
    
    # Iterate through the list to find the highest count of consecutive 1s
    max_length = 0
    current_length = 0
    
    for j in lst:
        if j == "1":
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
            
    print(max_length)
