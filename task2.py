import math
import time

import numpy as np
import numpy.ma as ma
from pyasn1.type.univ import Integer

database = [
    [1, 101, 2001, 2, 19.99, 1723062511.61],
    [2, 101, 2002, 1, 29.99, 1723069999.61],
    [3, 102, 2003, 5, 9.99, 172306123.61],
    [4, 103, 2001, 3, 19.99, 1723066729.61],
    [5, 104, 2004, 4, 49.99, 1723061254.61],
    [6, 105, 2002, 1, 29.99, 1723069857.61],
    [7, 101, 2005, 2, 39.99, 1723069857.61],
    [8, 102, 2003, 1, 9.99, 172306123.61],
    [9, 103, 2004, 0, 49.99, 1723062124.61],
    [10, 104, 2006, 1, 9.99, 1723069857.61]
]
db_array = np.array(database)


def total_revenue(arr):
    return np.multiply(arr[:, 3], arr[:, 4]).sum()


def unique_users_count(arr):
    return np.unique(arr[:, 1]).size


def most_purchased_product(arr):
    prod_quan_arr = arr[:, 2:4]
    sorted_arr = prod_quan_arr[np.argsort(prod_quan_arr[:, 0])].astype(int)

    most_popular_prod = [0, 0]
    current_prod = arr[1, 1]
    for ell in sorted_arr:
        prod_id = ell[0]
        total_quantity = 0

        if prod_id == current_prod:
            total_quantity += ell[1]
        else:
            current_prod = prod_id
            total_quantity = ell[1]

        if most_popular_prod[1] <= total_quantity:
            most_popular_prod[0] = current_prod
            most_popular_prod[1] = total_quantity
    return most_popular_prod[0]


def float_to_int(arr):
    return arr.astype(int)


def get_array_data_types(arr):
    types = []

    for element in db_array[0]:
        if np.dtype(element) == str:
            types.append("str")
        elif np.dtype(element) == int:
            types.append("int")
        elif np.dtype(element) == float and element % 1 != 0:
            types.append("float")
        elif np.dtype(element) == float and element % 1 == 0:
            types.append("int")

    return types


def product_and_quantity_array(arr):
    return arr[:, 2:4]


def get_user_transaction_count_array(arr):
    user_arr = arr[:, 1]
    sorted_arr = np.sort(user_arr).astype(int)

    user_trans_count_dict = {}
    for user in sorted_arr:
        if user_trans_count_dict.get(user) is None:
            user_trans_count_dict[user] = 1
        else:
            user_trans_count_dict[user] += 1

    return np.array(list(user_trans_count_dict.items()))


def get_masked_transactions(arr):
    return arr[arr[:, 3] > 1]


def increase_price(arr, value):
    return arr[:, 4] * value


def filter_transaction(arr):
    return arr[np.where(arr[:, 3] > 1)]


def revenue(arr, d1from, d1to, d2from, d2to, ):
    d1o_array = arr[np.where((arr[:, 5] < d1to))]
    revenue1 = d1o_array[np.where((d1o_array[:, 5] >= d1from))]

    d2o_array = arr[np.where((arr[:, 5] < d1to))]
    revenue2 = d2o_array[np.where((d2o_array[:, 5] >= d1from))]

    return np.array([revenue1, revenue2])


def get_user_transactions(arr, user_id):
    return arr[np.where(arr[:, 1] == user_id)]


def get_transactions_from_to(arr, dfrom, dto):
    to_array = arr[np.where((arr[:, 5] < dto))]
    return to_array[np.where((to_array[:, 5] >= dfrom))]


def top_five_products(arr):
    prod_revenue_arr = np.transpose(np.array([arr[:, 2], arr[:, 3] * arr[:, 4]]))
    prod_revenue_sorted_by_product_arr = prod_revenue_arr[np.argsort(prod_revenue_arr[:, 0])]

    unique_product_ids = np.unique(prod_revenue_sorted_by_product_arr[:, 0])
    total_revenues = np.array(
        [prod_revenue_sorted_by_product_arr[prod_revenue_sorted_by_product_arr[:, 0] == pid][:, 1].sum()
         for pid in unique_product_ids])

    prod_rev = np.column_stack((unique_product_ids, total_revenues))

    return prod_rev[np.argsort(prod_rev[:, 1])][1:6:1]


def print_array(message, arr):
    print(message + "\n" + str(arr) + "\n")


# Data Analysis Functions:
print_array("Total revenue function: ", total_revenue(db_array))
print_array("Unique users count function: ", unique_users_count(db_array))
print_array("Most purchased product function: ", most_purchased_product(db_array))
print_array("Float to int array: ", float_to_int(db_array))
print_array("Check data types:", get_array_data_types(db_array))

# Array Manipulation Functions:
print_array("Product quantity array function:", product_and_quantity_array(db_array))
print_array("User transaction count function: ", get_user_transaction_count_array(db_array))
print_array("Masked array function: ", get_masked_transactions(db_array))

# Arithmetic and Comparison Functions:
print_array("Price increase function: ", increase_price(db_array, 0.05))
print_array("Filter transaction function: ", filter_transaction(db_array))
print_array("Revenue comparison function: ",
            revenue(db_array, 1723062511.00, 1723062511.62, 1723062511.00, 1723062511.62))

# Indexing and Slicing Functions:
print_array("User transactions function: ", get_user_transactions(db_array, 101))
print_array("Data range slice function: ", get_transactions_from_to(db_array, 1723062511.00, 1723062511.62))

print_array("Top 5 products by revenue: ", top_five_products(db_array))
