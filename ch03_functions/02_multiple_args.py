"""

    02_multiple_args.py
    Using multiple positional and keyword args.

"""


def display_info(name, age, spouse, *children):
    print(len(children))
    print(name, age, spouse, children)


display_info('Bob', 37, 'Sally', 'Timmy', 'Johnny', 'Annie')


def display_info2(**family):
    print(family)


display_info2(name='Bob', age=37, spouse='Sally',
              child1='Timmy', child2='Johnny', child3='Annie')


def display_info3(greeting, *args, **kwargs):
    print(greeting, args, kwargs)


display_info3('hello', 10, ['stuff1', 'stuff2'], item1='value1', foo='bar')


# ---------unpacking arguments-------------------
def display_results(customer, purchase_amount):
    print('Customer: {first} {last}, amount: ${0:,.2f}'.format(purchase_amount, **customer))


cust = {
    'first': 'James',
    'last': 'Smith'
}

display_results(cust, 1108.23)
