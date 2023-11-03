class Calculator:
    def power(self, n, p):
        # Raise an error if either n or p are negative
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        # Otherwise, return the value of n raised to the power of p
        else:
            return n ** p
                
my_calculator = Calculator()
T = int(input("Enter number of test cases: "))

for _ in range(T):
    n, p = map(int, input("Enter n and p separated by space: ").split())
    try:
        # Try calculating the power and output the result
        ans = my_calculator.power(n, p)
        print(ans)
    except Exception as e:
        # Handle exceptions by outputting the error message
        print(e)
