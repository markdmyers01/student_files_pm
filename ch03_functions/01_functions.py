"""

    01_functions.py
    A Basic function in Python.

"""


def summary(customer, amount):
    return f'Customer: {customer.get("first")} {customer.get("last")}, amount: ${amount:,.2f}'


cust = {'first': 'James', 'last': 'Smith'}
results = summary(cust, 1108.23)
print(results)
