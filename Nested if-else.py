# Python Program to demonstrate Nested If-else

myAge = int(input('Enter age: '))
if myAge >= 18:
    myComment = "You can vote."
else:
    if myAge >= 10:
        myComment = "You are in middle school."
    else:
        if myAge >= 6:
            myComment = "You are in primary school."
        else:
            myComment = "You are too small to learn python"
print("At age: " + str(myAge) + "->" + myComment)

print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")