# Function to check if a number is prime
def is_prime(n):
    # Non-positive integers and 1 are not prime
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    # Multiples of 2 and 3 are not prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check for prime by testing only up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Main execution
def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        print("Prime" if is_prime(n) else "Not prime")

# Entry point of the script
if __name__ == "__main__":
    main()
