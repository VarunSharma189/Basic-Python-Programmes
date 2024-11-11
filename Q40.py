# write a python program to demonstrate various string methods

text = " Hello, World! "

# Changing case
lowercase_text = text.lower()      # " hello, world! "
uppercase_text = text.upper()      # " HELLO, WORLD! "
title_text = text.title()          # " Hello, World! "

# Trimming whitespace
stripped_text = text.strip()       # "Hello, World!"

# Splitting and joininguu
words = stripped_text.split(",")   # ['Hello', ' World!']
joined_text = "-".join(words)      # "Hello- World!"

# Replacing and finding
replaced_text = stripped_text.replace("World", "Python")  # "Hello, Python!"
index = stripped_text.find("World")   # 7
count = stripped_text.count("o")      # 2

# Print the results
print("Lowercase Text:", lowercase_text)
print("Uppercase Text:", uppercase_text)
print("Title Text:", title_text)
print("Stripped Text:", stripped_text)
print("Words:", words)
print("Joined Text:", joined_text)
print("Replaced Text:", replaced_text)
print("Index of 'World':", index)
print("Count of 'o':", count)

print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")
