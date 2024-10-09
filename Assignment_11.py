import numpy as np

# Create a 2D NumPy array
array = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])

print("Original Array:")
print(array)

# Accessing specific elements
print("\nAccessing specific elements:")
print("Element at row 1, column 2: ", array[1, 2])

# Accessing specific rows
print("\nAccessing specific rows:")
print("Row 1:", array[1])

# Accessing specific columns
print("\nAccessing specific columns: ")
print("Column 2:", array[:, 2])

# Slicing operations
print("\nSlicing operations:")
print("Subarray (first two rows and first three columns): ")
print(array[:2, :3])

# Boolean indexing
print("\nBoolean indexing: ")
boolean_mask = array > 5
print("Elements greater than 5: ")
print(array[boolean_mask])

# Fancy indexing
print("\nFancy indexing: ")
rows = np.array([0, 2])
columns = np.array([1, 3])
print("Elements at specific rows and columns: ")
print(array[rows[:, np.newaxis], columns])

# Extracting a subarray using fancy indexing
print("\nExtracting a subarray using fancy indexing: ")
fancy_indexed_array = array[[0, 1, 2], [1, 2, 3]]
print(fancy_indexed_array)
