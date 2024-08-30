# write a python code to demonstrate try and except(Exception Handling)
try:
    number = int(input("Enter a number:"))
    result = 10/number
    print(result)
except ZeroDivisionError:
    print("Error : Cannot Divide by zero.")
except ValueError:
    print("Error:Invalid Input. Please enter a valid number.")