# write a python code to print first n armstrong numbers that comes after the given number x
def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    armstrong_sum = sum(int(digit) ** power for digit in digits)
    return armstrong_sum == number

def find_n_armstrong_after_x(x, n):
    armstrong_numbers = []
    number = x + 1  
    while len(armstrong_numbers) < n:
        if is_armstrong(number):
            armstrong_numbers.append(number)
        number += 1
    return armstrong_numbers

# Example usage
x = int(input("Enter the starting number (x): "))
n = int(input("Enter how many Armstrong numbers (n) you want to find: "))

armstrong_numbers = find_n_armstrong_after_x(x, n)
print(f"The first {n} Armstrong numbers after {x} are: {armstrong_numbers}")
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")