"""

    baseball.py
    This file accompanies task3_1_starter.py.

"""
from collections import namedtuple
import sys


def salary_sort(sal_record):
    return sal_record.salary


# Step 1.
# Migrate the code that reads the People.csv and Salaries.csv data
# into this file.  You can optionally use your solution from earlier instead.
#
# You should create a function called load_data() that accepts the filenames
# to read as well as the year the user desires to see the salaries of.
# For example:
#
#    def load_data(salary_filepath, people_filepath, year):
#        # return loaded data
