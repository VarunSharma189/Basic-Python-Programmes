# Write a python program to demonstrate try, except and else
try:
    number = int(input("Enter a number:"))
    result = 10/number
except ZeroDivisionError:
    print("Error : Cannot Divide by zero.")
except ValueError:
    print("Error:Invalid Input. Please enter a valid number.")
else:
    print(f"The Result is {result}")    
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP:-0221BCA136")
