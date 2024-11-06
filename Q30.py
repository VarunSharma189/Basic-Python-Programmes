def calculate_discount(bill_amt):
    # Initialize sum of digits
    sum_digits = 0
    temp_amt = bill_amt
    
    # Calculate sum of digits using a while loop
    while temp_amt > 0:
        digit = temp_amt % 10  # Get the last digit
        sum_digits += digit    # Add it to sum_digits
        temp_amt //= 10        # Remove the last digit
    
    # The sum of digits is treated as the discount percentage
    discount_percentage = sum_digits
    
    # Calculate the discount amount
    discount_amount = (bill_amt * discount_percentage) / 100
    
    # Subtract the discount from the total bill
    final_bill = bill_amt - discount_amount
    
    return discount_percentage, discount_amount, final_bill

# Example usage
bill_amt = int(input("Enter the total bill amount: "))
discount_percentage, discount_amount, final_bill = calculate_discount(bill_amt)
print(f"Original Bill Amount: {bill_amt}")
print(f"Discount Percentage: {discount_percentage}%")
print(f"Discount Amount: {discount_amount}")
print(f"Final Bill Amount: {final_bill}")
