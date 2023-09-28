"""

      task3_1_starter.py   -   Modules and Functions

      This was the solution from task2_1.py.  If you run it, you will see it
      currently runs as is.

      Work from this file or replace it with your own previous solution.

      Your task: Create a load_data() function in the ch03_functions/baseball.py file
                 that loads the data from the two provided files and returns a data structure
                 that can be displayed in this file.


      Step 1. Either use this file or make a copy of your own task2_1_starter.py file.
              Create a load_data() function in baseball.py

      Step 2. Migrate the code that reads from the files into the load_data() function.

      Step 3. Remove unnecessary code from this file now.

      Step 4. Import baseball.py into this file.
              (You should be able to say "import baseball" if the current directory is listed
               in your sys.path.  Then baseball.load_data() should work)
              Invoke the load_data() function from that file.

      Step 5. Test your solution to ensure it works.

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
top_sals = []

def salary_sort(sal_record):
    return sal_record.salary

filepath = os.path.join(working_dir, salaries_filename)
people_filepath = os.path.join(working_dir, people_filename)


year_str = input('Enter a year (1985-2016): ')

try:
    with open(filepath, encoding='utf-8') as f_sal:
        header = f_sal.readline().strip().split(',')
        SalaryRecord = namedtuple('SalaryRecord', header)

        for line in f_sal:
            data = line.strip().split(',')
            if year_str == data[0]:
                try:
                    data[4] = int(data[4])
                except ValueError:
                    data[4] = 0

                sal_rec = SalaryRecord(*data)
                salaries.append(sal_rec)
except IOError as err:
    print(err, file=sys.stderr)
    sys.exit()

try:
    with open(people_filepath, encoding='utf-8') as f_people:
        for line in f_people:
            data = line.strip().split(',')
            player_id, first_name, last_name = data[0], data[13], data[14]
            players[player_id] = (first_name, last_name)
except IOError as err:
    print(err, file=sys.stderr)
    sys.exit()

salaries.sort(key=salary_sort, reverse=True)


how_many = 10
print_header = ['Name', 'Salary', 'Year']
print('{0:35}{1:<20}{2:10}'.format(*print_header))

for salary_record in salaries[:how_many]:
    player_id = salary_record.playerID
    (first_name, last_name) = players[player_id]
    name = first_name + ' ' + last_name
    salary = f'${salary_record.salary:<19,.2f}'
    year = salary_record.yearID

    print(f'{name:35}{salary:<}{year:<10}')
