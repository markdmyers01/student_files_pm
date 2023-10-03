"""

    01_basics.py
    A basic Python Class

"""




class Contact:
    def __init__(self, name='', address=''):
        self.name = name
        self.address = address

    def __str__(self):
        return f'({self.name}, {self.address})'


c = Contact('John Smith', '123 Main St.')
print(c.name)
print(c, type(c))
c.name = 'Joe Jones'
print(c.name)
c.foo = [1, 2, 3]
print(c.foo)

# d = Contact('John Smith', '123 Main St.')
# print(d.foo)
