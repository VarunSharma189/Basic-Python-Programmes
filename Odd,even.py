'''Write a python code to print the numbers in 3 configurations:
1) Even
2) Odd
3) Divisible by 5
From num1 to num2'''
 
def print_numbers(num1, num2):
    even_numbers = []
    odd_numbers = []
    divisible_by_5 = []

    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        if num % 2 != 0:
            odd_numbers.append(num)
        if num % 5 == 0:
            divisible_by_5.append(num)

    print("Even numbers:")
    print(even_numbers)
    
    print("Odd numbers:")
    print(odd_numbers)
    
    print("Numbers divisible by 5:")
    print(divisible_by_5)

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print_numbers(num1, num2)