"""

    02_properties.py
    Python properties.

"""


class Contact:
    def __init__(self, name='', address='', email=''):
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return f'{self.name} {self.address}'

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = ''
        if '@' in email:
            self._email = email


c = Contact('Bob', '123 Main St.', 'bobmail')
print(f'Bob\'s email: {c.email}')
c.email = 'bob@yahoo.com'
print(f'Bob\'s email: {c.email}')
