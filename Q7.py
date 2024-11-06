my_string ="Bharati"
char_to_find = input("Enter the character you want to find: ")
positions = [ i for i , char in enumerate(my_string)if char == char_to_find]

if positions:
    print(f"The character'{char_to_find}' is found at position:{positions}")

else:
    print(f"The character'{char_to_find}' is not found in the string ")
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")
