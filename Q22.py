# Python program to print result of the student

Roll_no = int(input("Please enter your roll no:"))
Name =  input("Please enter your Name:")
Class = input("Please enter your Class:")
print('\n')

print("Now Please enter all your marks as asked :-")
eng_marks = int(input("Enter your english marks: "))
math_marks = int(input("Enter your Mathematics marks: "))
sci_marks = int(input("Enter your Science marks: "))
Ss_marks = int(input("Enter your Social Science marks: "))
Comp_marks = int(input("Enter your Computer marks: ")) 
sum = eng_marks+math_marks+sci_marks+Ss_marks+Comp_marks 

print('\n')
print(f"Roll No:     {Roll_no}")
print(f"Name:        {Name}")
print(f"Class:       {Class}")

print('---------------------------------------------------------')
print("Subject         Final Marks        Obtained Marks")
print('---------------------------------------------------------')
print(f"English           100                {eng_marks}")          
print(f"Mathematics       100                {math_marks}")          
print(f"Science           100                {sci_marks}")          
print(f"Social Science    100                {Ss_marks}")          
print(f"Computer          100                {Comp_marks}")  
print("---------------------------------------------------------")    
print(f"Total             500                {sum}")    
print("---------------------------------------------------------")    
marks = sum/5
if marks >= 80:
    print("Grade: O")
    print(f"Percentage: {marks}")
elif marks >=70:
    print("Grade: A+")
    print(f"Percentage: {marks}")
elif marks >=60:
    print("Grade: A")
    print(f"Percentage: {marks}")
elif marks >=50:
    print("Grade: B")
    print(f"Percentage: {marks}")
elif marks >=40:
    print("Grade: C")
    print(f"Percentage: {marks}")
else:
    print("Grade: E")
    print(f"Percentage: {marks}")
print("---------------------------------------------------------") 

print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")
