"""

    02_ctxmgr01.py
    Before and after using the 'with' control

"""
import sys

lines = []
try:
    f = open('alice.txt', encoding='utf-8-sig')
    try:
        lines = f.readlines()
    finally:
        f.close()
except IOError as err:
    print(f'Handled {err}', file=sys.stderr)

print(f'{len(lines)} lines read.')


lines = []
try:
    with open('alice.txt', encoding='utf-8-sig') as f:
        lines = f.readlines()
except IOError as err:
    print(f'Handled {err}', file=sys.stderr)

print(f'{len(lines)} lines read.')
