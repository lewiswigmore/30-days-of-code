class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        # Calculate the sum of divisors for a given number n.
        divisors = []  # Initialize an empty list to store divisors.
        for i in range(1, n + 1):
            if n % i == 0:  # Check if i is a divisor of n.
                divisors.append(i)  
        return sum(divisors)  

n = int(input())  # Read an integer input.
my_calculator = Calculator()  # Create an instance of the Calculator class.
s = my_calculator.divisorSum(n)  
print("I implemented: " + type(my_calculator).__bases__[0].__name__) 
print(s)  
