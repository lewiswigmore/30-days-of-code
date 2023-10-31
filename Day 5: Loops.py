if __name__ == '__main__':
    # Read an integer 'n' from user input
    n = int(input().strip())
    
    # Loop from 1 to 10 and print the multiplication table for 'n'
    for i in range(1, 11):
        # Print the equation and result for each multiplication
        print(str(n) + " x " + str(i) + " = " + str(n * i))
