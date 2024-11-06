# write a python program to swap values of two variables using various methods

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
 
# code to swap 'x' and 'y' using third variable
temp = x
x = y
y = temp

# code to swap 'x' and 'y' using multiple or group assignment
x,y = y,x

# code to swap 'x' and 'y' without using third variable
x = x+y
y = x-y
x = x-y

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
