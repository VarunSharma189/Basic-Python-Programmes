# Write a python program to print the sum of cube of prime numbers between a given range

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

def sum_of_cubes_of_primes(start, end):
    sum_cubes = 0
    for num in range(start, end + 1):
        if is_prime(num):
            sum_cubes += num ** 3
    return sum_cubes

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
result = sum_of_cubes_of_primes(start, end)
print(f"The sum of cubes of prime numbers between {start} and {end} is: {result}")
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")
