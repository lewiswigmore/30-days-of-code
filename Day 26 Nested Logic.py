def calculate_fine(actual_date, expected_date):
    actual_day, actual_month, actual_year = actual_date
    expected_day, expected_month, expected_year = expected_date
    
    # Book is returned after the expected year
    if actual_year > expected_year:
        return 10000
    # Book is returned within the expected year but after the expected month
    elif actual_year == expected_year and actual_month > expected_month:
        return 500 * (actual_month - expected_month)
    # Book is returned within the expected month but after the expected day
    elif actual_year == expected_year and actual_month == expected_month and actual_day > expected_day:
        return 15 * (actual_day - expected_day)
    # Book is returned on or before the expected date
    else:
        return 0

# Main execution
def main():
    actual_date = list(map(int, input().strip().split(' ')))
    expected_date = list(map(int, input().strip().split(' ')))
    fine = calculate_fine(actual_date, expected_date)
    print(fine)

# Entry point of the script
if __name__ == "__main__":
    main()
