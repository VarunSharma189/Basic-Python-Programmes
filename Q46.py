# Write a python program to print the prime, perfect and armstrong number just smaller to the given input numbers

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        print(n)
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    print(n)
    return True

def is_perfect(n):
    if n < 2:
        return False
    
    divisors_sum = 1  # 1 is a proper divisor for any number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    
    return divisors_sum == n

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    sum_of_powers = 0
    
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    if sum_of_powers == number:
        return True
    else:
        return False
    
def largest_prime_smaller_than(n):
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return None

def largest_perfect_smaller_than(n):
    for i in range(n - 1, 1, -1):
        if is_perfect(i):
            return i
    return None

def largest_armstrong_smaller_than(n):
    for i in range(n - 1, 0, -1):
        if is_armstrong(i):
            return i
    return None

num = int(input("Enter a number: "))

prime_smaller = largest_prime_smaller_than(num)
perfect_smaller = largest_perfect_smaller_than(num)
armstrong_smaller = largest_armstrong_smaller_than(num)

print(f"Largest prime number smaller than {num}: {prime_smaller}")
print(f"Largest perfect number smaller than {num}: {perfect_smaller}")
print(f"Largest Armstrong number smaller than {num}: {armstrong_smaller}")
print("Written by Naman ERP :- 009")