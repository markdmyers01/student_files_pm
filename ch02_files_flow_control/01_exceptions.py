"""

    01_exceptions.py
    Exception Handling.

"""
import sys

# Example 1:  Handling a basic exception
# print('Example 1: Basic Exceptions')
# a = input('Number 1: ')
# b = input('Number 2: ')
# try:
#     a = float(a)
# except ValueError:
#     a = 0
# try:
#     b = float(b)
# except ValueError:
#     b = 0
# result = a / b                           # Yikes!  This one can still bite us!
# print(f'Division result is: {result}\n')


# Example 2:  Handling multiple exceptions
# print('\nExample 2: Multiple Exceptions')
# a = input('Number 1: ')
# b = input('Number 2: ')
# result = 'undefined'
# try:
#     result = float(a) / float(b)
# except ValueError:
#     pass
# except ZeroDivisionError:
#     pass
# print(f'Division result is: {result}\n')


# # Example 3: Grouping Exceptions
# print('Example 3: Grouping Exceptions')
# a = input('Number 1: ')
# b = input('Number 2: ')
# result = 'undefined'
# try:
#     result = float(a) / float(b)
# except (ValueError, ZeroDivisionError):
#     pass
# print(f'Division result is: {result}\n')


# Example 4:  Generic Exception Handling
# print('Example 4: Generic Handling')
# a = input('Number 1: ')
# b = input('Number 2: ')
# result = 'undefined'
# try:
#     result = float(a) / float(b)
# except:
#     typ, value, tb = sys.exc_info()
#     print(typ)
#     print(f'A {typ.__name__} occurred: {value}')
# print(f'Division result is: {result}\n')
#
# x = 10
# print(type(x))

# Example 5:  The Exception Object
print('Example 5: The Exception Object')
a = input('Number 1: ')
b = input('Number 2: ')
result = 'undefined'
try:
    result = float(a) / float(b)
except Exception as err:
    print(f'A {type(err).__name__} occurred: {err}', file=sys.stderr)
    sys.exit(1)

print(f'Division result is: {result}')
