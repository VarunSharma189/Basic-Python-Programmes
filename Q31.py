# write a python code to reverse the digits of a given number without using any built in function
def reverse_number(number):
    reversed_num = 0
    while number:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    return reversed_num

number = int(input("Enter any number: "))
print("Reversed Number:", reverse_number(number))
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")