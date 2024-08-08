import math
import time

import numpy as np

database = [
    [1, 101, 2001, 2, 19.99, 1723062511.61],
    [2, 101, 2002, 1, 29.99, 1723062124.61],
    [3, 102, 2003, 5, 9.99, 172306123.61],
    [4, 103, 2001, 3, 19.99, 1723066729.61],
    [5, 104, 2004, 4, 49.99, 1723061254.61],
    [6, 105, 2002, 1, 29.99, 1723069857.61],
    [7, 101, 2005, 2, 39.99, 1723069857.61],
    [8, 102, 2003, 1, 9.99, 172306123.61],
    [9, 103, 2004, 0, 49.99, 1723062124.61],
    [10, 104, 2005, 0, 39.99, 1723069857.61]
]
db_array = np.array(database)


def total_revenue(arr):
    return np.multiply(arr[:, 3], arr[:, 4]).sum()


def unique_users_count(arr):
    return np.unique(arr[:, 1]).size


def product_and_quantity_dict(arr):
    product_ids = arr[:, 2]
    quantities = arr[:, 3]

    prod_quan_dict = {}
    for i in range(product_ids.size):
        product_id = product_ids[i]
        quantity = quantities[i]

        if prod_quan_dict.get(product_id) is None:
            prod_quan_dict[product_ids[i]] = quantity
        else:
            prod_quan_dict[product_id] = prod_quan_dict.get(product_id) + quantity

    return prod_quan_dict


def most_purchased_product(arr):
    prod_quan_dict = product_and_quantity_dict(arr)
    return max(prod_quan_dict, key=prod_quan_dict.get)


def float_to_int(number):
    return round(number)


# TODO
def get_array_data_types(arr):
    types = []

    for element in db_array[0]:
        if type(element) == str:
            types.append("str")
        elif type(element) == int:
            types.append("int")
        elif type(element) == float and element % 1 == 0:
            types.append("float")
        elif type(element) == float and element % 1 != 0:
            types.append("int")

    return types


def product_and_quantity_array(arr):
    prod_and_quan = product_and_quantity_dict(arr)

    return np.array(list(zip(list(prod_and_quan.keys()), list(prod_and_quan.values()))))


def get_user_transaction_count_array(arr):
    user_ids = arr[:, 1]
    user_trans_count_dict = {}
    for i in range(user_ids.size):
        user_id = user_ids[i]

        if user_trans_count_dict.get(user_id) is None:
            user_trans_count_dict[user_ids[i]] = 1
        else:
            user_trans_count_dict[user_id] = user_trans_count_dict.get(user_id) + 1

    return np.array(list(zip(list(user_trans_count_dict.keys()), list(user_trans_count_dict.values()))))


def get_masked_transactions(arr):
    empty_transactions = []
    for i in range(arr.shape[0]):
        if arr[i, 3] == 0:
            empty_transactions.append(i)

    return np.delete(arr, empty_transactions, 0)


def increase_price(arr, value):
    arr[:, 4] *= value
    return arr


def filter_transaction(arr):
    transactions = []
    for i in range(arr.shape[0]):
        if arr[i, 3] < 2:
            transactions.append(i)

    return np.delete(arr, transactions, 0)


# TODO
# Revenue Comparison Function: Create a function to compare the revenue from
# two different time periods.
def revenue():
    return 0


def get_user_transactions(arr, user_id):
    transactions = []

    for i in range(arr.shape[0]):
        if arr[i, 1] == user_id:
            transactions.append(list(arr[i]))

    return transactions


# TODO
# Date Range Slicing Function: Develop a function to slice the dataset to include
# only transactions within a specific date range.
def get_transactions_from_to(arr, from_v, to):
    return 0


# TODO
# Top Products Function: Implement a function using advanced indexing to retrieve
# transactions of the top 5 products by revenue.

def print_array(arr, message=None):
    if message is not None:
        print(message + str(arr))
    else:
        print(arr)


# TODO print a
