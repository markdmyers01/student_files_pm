"""

    01_functions.py
    A Basic function in Python.

"""
import os
from os import listdir, path

x = path.abspath('01_functions.py')
print(x)

def summary(customer, amount):
    return f'Customer: {customer.get("first")} {customer.get("last")}, amount: ${amount:,.2f}'


cust = {'first': 'James', 'last': 'Smith'}

results = summary(cust, 1108.23)
print(results)
