import numpy as np

listOfFruits = ["Apple", "Mango", "Banana"]
arrayOfFruits = np.array(listOfFruits)
print("Array of Fruits: ")
print(arrayOfFruits)
newArrayOfFruits = np.append(arrayOfFruits, "Pear")
print("Append a new element: ")
print(newArrayOfFruits)

zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
range_array = np.arange(0, 10, 2)  # Array of even numbers from 0 to 8

def display_arrays():
    print("Zeros Array (2x3):")
    print(zeros_array)
    
    print("\nRange Array (0 to 10 with step 2):")
    print(range_array)

display_arrays()

def show_attributes(array, name):
    print(f"\nAttributes of {name}:")
    print(f" - Shape: {array.shape}")
    print(f" - Data type: {array.dtype}")
    print(f" - Number of elements: {array.size}")

show_attributes(zeros_array, "zeros_array")
show_attributes(range_array, "range_array")