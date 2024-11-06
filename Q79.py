#Wap in py to demonstrate decorators 

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Add functionality before calling the original function
        result = original_function(*args, **kwargs)
        # Add functionality after calling the original function
        return result
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")