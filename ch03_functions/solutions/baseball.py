from collections import namedtuple
import sys


def salary_sort(sal_record):
    return sal_record.salary


def load_data(salaries_filepath, people_filepath, input_year='1985'):
    salaries = []
    players = {}
    top_sals = []

    try:
        with open(salaries_filepath, encoding='utf-8') as f_sal:
            header = f_sal.readline().strip().split(',')
            SalaryRecord = namedtuple('SalaryRecord', header)

            for line in f_sal:
                data = line.strip().split(',')
                if input_year == data[0]:
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

    for sal_info in salaries:
        year = sal_info.yearID
        salary = sal_info.salary
        playerid = sal_info.playerID
        player_data = players.get(playerid)
        if player_data:
            first_name, last_name = player_data
            top_sals.append((first_name, last_name, salary, year))

    return top_sals
