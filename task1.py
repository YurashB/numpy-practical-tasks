import numpy as np

one_dim_array = np.arange(0, 11, dtype=int)  # create 1-D array

two_dim_array = np.arange(1, 10).reshape(3, 3)  # create 2-D array

print("Third element of the 1-D array: ",
      one_dim_array[2])  # Access and print the third element of the one-dimensional array.

print("Slice first 2 col and rows:\n",
      two_dim_array[:2, :2])  # Slice and print the first two rows and columns of the two-dimensional array.

print("Add 5 two each element in 1-D array:", one_dim_array + 5)  # Add 1 two each element in 1-D array

print("Multiple 2 to each element in 2-D array:\n", two_dim_array * 2)  # Multiple 2 to each element in 2-D array


def print_array(arr, message=None):  # Function to print array
    if message is not None:
        print(message + str(arr))
    else:
        print(arr)


one_dim_array = np.arange(1, 10)
two_dim_array = np.arange(1, 10).reshape(3, 3)
print_array(one_dim_array[2], message="Third element: ")
print_array(two_dim_array[:2, :2], message="Slice first 2 col and rows:\n")
print_array(one_dim_array + 5, message="Add 5 two each element in 1-D array:")
print_array(two_dim_array * 2, message="Multiple 2 to each element in 2-D array:\n")
