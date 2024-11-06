#Demonstate comments and documentation in Python
"""
This script provides example of single line comments, multiline comments and docstrings
"""
def add(a,b):
 """
      Returns the sum of a and b.
      Parameters:
      a(int, float): First number.
      b(int, float): Second number

       Returns:
        int,float: sum of a and b.
    """
 return a + b

def subtract(a, b):


 """
   Returns the diffrence of a and b.
    Parameters:
    a(int, float): First number.
    b(int, float): Second number

    Returns:
        int,float: diffrence of a and b.

  """
 return a-b

 #Main part of the script

if __name__ == "__main__":
      x,y = 10,5 #Initialize variables

#Perform operation and print results

print(f"The sum of {x} and {y} is {add(x,y)}")
print(f"The diffrence of {x} and {y} is {subtract(x,y)}")  #Subtraction

'''
End of the script: Demonstrated single- line comments, multi-line comments, and docstrings
'''

print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")
