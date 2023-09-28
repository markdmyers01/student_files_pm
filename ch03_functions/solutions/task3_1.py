"""

      task3_1.py   -   Modules and Functions

      Partially modularizes task2_1 by creating a load_data()
      function within baseball.py

"""
import os

import baseball     # assumes current directory is included in sys.path otherwise use:  from ch03_functions.solutions import baseball as baseball

working_dir = '../../resources/baseball/'
people_filename = 'People.csv'
salaries_filename = 'Salaries.csv'

year_str = input('Enter a year (1985-2016): ')

sal_filepath = os.path.join(working_dir, salaries_filename)
people_filepath = os.path.join(working_dir, people_filename)


top_sals = baseball.load_data(sal_filepath, people_filepath, year_str)


how_many = 10
print_header = ['Name', 'Salary', 'Year']
print('{0:35}{1:<20}{2:10}'.format(*print_header))

for salary_info in top_sals[:how_many]:
    first_name = salary_info[0]
    last_name = salary_info[1]
    name = first_name + ' ' + last_name
    salary = f'${salary_info[2]:<19,.2f}'
    year = salary_info[3]

    print(f'{name:35}{salary:<}{year:<10}')
