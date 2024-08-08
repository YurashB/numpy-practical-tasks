import numpy as np

array = np.random.randint(1, 100, (6, 6))


def transpose(arr):
    return np.transpose(arr)


def reshape(arr, new_shape):
    return np.reshape(arr, new_shape)


def split(arr, indices_or_sections, axis):
    return np.split(arr, indices_or_sections, axis)


def combine(*args):
    return np.concatenate(args)


def print_array(arr, message=None):
    if message is not None:
        print(message + str(arr))
    else:
        print(arr)
    print()


print_array(array, "Initial array:\n")
print_array(transpose(array), "Transpose func result:\n")
print_array(reshape(array, (3, 12)), "Reshape func result:\n")
print_array(split(array, 3, 1), "Split func result:\n")
print_array(combine(array, array), "Combine func result:\n")
