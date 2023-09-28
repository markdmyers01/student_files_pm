"""

    07_using_csv.py
    The CSV module.

"""
import csv
import sys


airports = []
try:
    with open('../resources/airports.dat', encoding='utf8') as f:
        try:
            for row in csv.reader(f):
                airports.append(row)
                print(row)
        except csv.Error as err:
            print(f'Error: {err}', file=sys.stderr)
except IOError as err:
    print(err, file=sys.stderr)

try:
    with open('first100.dat', 'w', encoding='utf8') as f:
        try:
            csv.writer(f).writerows(airports[1:101])
        except csv.Error as err:
            print(f'Error: {err}', file=sys.stderr)
except IOError as err:
    print(err, file=sys.stderr)
