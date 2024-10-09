import numpy as np

# Creating a 1D array
array = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("Original Array:")
print(array)

# Reshaping the array into a 3D array (2x2x2)
reshaped_array = array.reshape(2, 2, 2)
print("\nReshaped Array (2x2x2):")
print(reshaped_array)
print("\n")
# Transposing the reshaped array
transposed_array = reshaped_array.transpose()
print("Transposed Array:")
print(transposed_array)
print("\n")

# Swapping axes of the array
swapped_axis_0_1 = reshaped_array.swapaxes(0, 1)
swapped_axis_1_2 = reshaped_array.swapaxes(1, 2)

print("Swapped Axis 0 and 1:")
print(swapped_axis_0_1)
print("\n")
print("Swapped Axis 1 and 2:")
print(swapped_axis_1_2)
