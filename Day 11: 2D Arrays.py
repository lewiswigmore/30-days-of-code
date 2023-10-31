if __name__ == '__main__':
    arr = []

    # Read a 6x6 matrix from user input and store it in 'arr'.
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -float('inf')
    for i in range(1, 5):
        for j in range(1, 5):
            # Calculate the hourglass sum.
            hourglass_sum = 0
            hourglass_sum += arr[i][j]
            hourglass_sum += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            hourglass_sum += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]

            # Check if the current hourglass sum is greater than the maximum.
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum

    # Print the maximum hourglass sum.
    print(max_sum)
