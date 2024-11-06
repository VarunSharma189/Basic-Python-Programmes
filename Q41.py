# WAP to initialize a string to perform various operations. Also, demonstrate raw and formatted string

# Initializing a string
original_text = " Python Programming "

# Trimming whitespace
trimmed_text = original_text.strip()

# Changing case
lowercase_text = trimmed_text.lower()
uppercase_text = trimmed_text.upper()

# Replacing substrings
replaced_text = trimmed_text.replace("Python", "Java")

# Splitting and joining
words = trimmed_text.split()
joined_text = "-".join(words)

# Formatting strings
name = "Alice"
language = "Python"
formatted_string = f"{name} loves {language}"

# Output the results
print("Original Text:", original_text)
print("Trimmed Text:", trimmed_text)
print("Lowercase Text:", lowercase_text)
print("Uppercase Text:", uppercase_text)
print("Replaced Text:", replaced_text)
print("Words:", words)
print("Joined Text:", joined_text)
print("Formatted String:", formatted_string)

# Normal string with escape characters
normal_string = "This is a newline character: \n"

# Raw string
raw_string = r"This is a newline character: \n"

print("Normal String:", normal_string)
print("Raw String:", raw_string)

# Output:
# Normal String: This is a newline character:
# Raw String: This is a newline character: \n

print("Written by Naman ERP :- 009")