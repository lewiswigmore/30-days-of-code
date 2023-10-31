def solve(meal_cost, tip_percent, tax_percent):
    # Calculate amounts
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    total_cost = meal_cost + tip + tax
    
    # Print the total cost after rounding it to the nearest integer
    print(round(total_cost))

if __name__ == '__main__':
    # Read the meal cost, tip percentage, and tax percentage from user input.
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    
    # Call the solve function to calculate and print the total cost
    solve(meal_cost, tip_percent, tax_percent)
