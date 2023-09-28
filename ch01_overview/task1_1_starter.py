"""
    task1_1_starter.py

    This script performs a temperature conversion.  You may provide a
    command-line argument to the script in the form:

        python task1_1_starter.py 78

    Or you may run the script without arguments and the default value of 100
    will be used:

        python task1_1_starter.py
"""
import sys

user_input = '100'
if len(sys.argv) > 1:
    user_input = sys.argv[1]

print(sys.argv)

try:
    f_temp = float(user_input)
    c_temp = (f_temp - 32) * 5.0 / 9.0
    degree_symbol = '\u00b0'
    print(f'{f_temp:3.1f}{degree_symbol}F  = {c_temp:3.1f}{degree_symbol}C')
except ValueError:
    print(f'{user_input} must be a numeric value')
