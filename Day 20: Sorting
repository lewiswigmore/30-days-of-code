if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    
    # Initialize the count of swaps to 0.
    numSwaps = 0
    
    # Perform n passes over the array.
    for i in range(n):
        # In each pass, go through the array up to the n-1 element.
        for j in range(n - 1):
            # If the current element is greater than the next element, swap them.
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                # Increment the swap counter.
                numSwaps += 1
    
    # After sorting, print the number of swaps, first element, and last element.
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
