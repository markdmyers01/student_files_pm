"""

      task2_1_starter.py   -   Baseball player salaries

      Reads data from multiple files.  Determines the top salaries for
      a specified year between 1985 and 2016.

      Salaries.csv file format:  yearID,teamID,lgID,playerID,salary
      People.csv   file format:  playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID

"""
from collections import namedtuple
import os
import sys

working_dir = '../resources/baseball/'
people_filename = 'People.csv'
salaries_filename = 'Salaries.csv'

input_year = 0
salaries = []
players = {}


def salary_sort(sal_record):
    return sal_record.salary


# Step 1. Ask user (input) to determine the year to search for.


# Step 2. Join the working_dir and salaries_filename using os.path.join().
#         Using a with control, open the salary file.

#         One approach for reading data is to use the header from the Salaries.csv file.
#         To do this, you must read the first line from the file, split it, and provide it
#         to the namedtuple() constructor

#             header = f_sal.readline().split(',')
#             SalaryRecord = namedtuple('SalaryRecord', header)

#         Now in a for loop, read the remaining records from the file
#         placing each record into a namedtuple.  Append each namedtuple
#         into the provided salaries list if the year matches
#         the year requested by the user.


# Step 3. Read player records from the people file (People.csv).
#         Store each record in the provided players dictionary.
#         Hint:  Use players[playerid] = player_record
#                where playerid is the first field in each record
#                      and player_record is the player's data


# Step 4. Sort the salaries list by-salary using the provided function above.
#
#         Hint: Use  salaries.sort(key=salary_sort)


# Step 5. With the salaries list sorted in order by salary, you can get the top
#         salaries now.  For each salary, you will need to get the playerid
#         and then use the playerid to access the dictionary to get the player's
#         first and last name


# Step 6. Print the first and last name of each player as well as the salary and year.

