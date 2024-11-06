# Python code to demonstrate Numpy Library
import numpy as np

# Creating 1D arrays
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

# Element wise addition of two arrays
sum_arrays = array_a + array_b  # Output: [5, 7, 9]

# Calculating the mean of the elements in array_a
mean_value = np.mean(array_a)  # Output: 2.0

# Calculating the standard deviation of the elements in array_a
std_dev = np.std(array_a)  # Output: 0.8165

# Display Results
print(f"Array Sum: {sum_arrays}")
print(f"Mean of array: {mean_value}")
print(f"Standard deviation of array: {std_dev}")

print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")
