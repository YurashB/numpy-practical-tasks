from datetime import datetime
import os

import numpy as np

array = np.random.randint(1, 100, (10, 10))


def save(arr, path="arrays", fm="txt"):
    if not os.path.exists(path):
        os.makedirs(path)

    file_name = path + "/array_saving_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if fm == "txt":
        np.savetxt(file_name + ".txt", arr)
    elif fm == "csv":
        np.savetxt(file_name + ".csv", arr, delimiter=",")
    elif fm == "npy":
        np.save(file_name + ".npy", arr)
    elif fm == "npz":
        np.savez(file_name + ".npz", arr)
    else:
        raise Exception("Can`t save in format format [" + fm + "]")

    return file_name


def load(file_name):
    _, extension = os.path.splitext(file_name)

    if extension == ".txt":
        return np.loadtxt(file_name)
    elif extension == ".csv":
        return np.loadtxt(file_name, delimiter=",")
    elif extension == ".npy":
        return np.load(file_name)
    elif extension == ".npz":
        npz_file = np.load(file_name)
        arrays = [npz_file[name] for name in npz_file.files]
        npz_file.close()
        return np.concatenate(arrays)
    else:
        raise Exception("Can`t load such file [" + file_name + "]")


def sum(arr):
    return np.sum(arr)


def mean(arr):
    return np.mean(arr)


def median(arr):
    return np.median(arr)


def standard_deviation(arr):
    return np.std(arr)


def wise_sum(arr, axis=1):
    if axis != 0 and axis != 1:
        raise Exception("Invalid axis direction, can be 0(column) or 1(row)")
    else:
        return np.sum(arr, axis)


def wise_mean(arr, axis=1):
    if axis != 0 and axis != 1:
        raise Exception("Invalid axis direction, can be 0(column) or 1(row)")
    else:
        return np.mean(arr, axis)


def wise_median(arr, axis=1):
    if axis != 0 and axis != 1:
        raise Exception("Invalid axis direction, can be 0(column) or 1(row)")
    else:
        return np.median(arr, axis)


def wise_std(arr, axis=1):
    if axis != 0 and axis != 1:
        raise Exception("Invalid axis direction, can be 0(column) or 1(row)")
    else:
        return np.std(arr, axis)


def print_array(arr, message=None):
    if message is not None:
        print(message + str(arr))
    else:
        print(arr)
    print()


print_array(array, "Initial array:\n")

# Saving
# todo
save(array, "txt")

