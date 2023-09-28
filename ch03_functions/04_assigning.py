"""

    04_assigning.py
    Attempting to manipulate (modify) a global variable)

"""
values = list(range(100))
num_records = 5


def change_records():
    num_records = 10               # doesn't change value of num_records


def display_records():
    print(values[:num_records])


change_records()
display_records()


# ---------------------------------------------------------------
def change_records():
    global num_records
    num_records = 10               # does change value of num_records


def display_records():
    print(values[:num_records])


change_records()
display_records()


# --------------------------------------------------------------
def change_records():
    globals()['num_records'] = 10  # does change value of num_records


def display_records():
    print(values[:num_records])


change_records()
display_records()
