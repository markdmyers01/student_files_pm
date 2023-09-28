"""

    01_styleguide.py
    Illustrates some of the PEP 8 rules.

"""
import os, sys      # not on one line
import os           # this is better
import sys


from datetime import datetime

if datetime.now().isoweekday() == 1:
    print("TGIM!")                                  # Indentations with 4 spaces.  Stick to it.


greet, Greet, GREET = 'hello', 'howdy', 'hola'      # identifiers are case-sensitive

say_hello = 'hi'                                    # underscores to separate identifier words
say_hello2 = 'Hi'
print(say_hello == say_hello2)


def my_func():                                      # underscores for function names
    print(say_hello)


days = [                                            # preferred closing bracket alignment, same for parens and curlies
    1, 2, 3
]

days2 = [                                           # this is okay too
    1, 2, 3
    ]

days3 = [1, 2, 3]


class SomeFunClass(object):                         # use CapWords notation for class names
    pass


def my_func2(arg1, arg2, arg3, arg4,
             arg5, arg6):                           # start arguments beneath other arguments
    pass
