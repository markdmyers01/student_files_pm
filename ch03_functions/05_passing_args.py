"""

    05_passing_args.py
    Passing mutable vs immutable arguments.

"""


def update_values(v1, v2):
    v1 *= 2
    v2 *= 2


values1 = (1, 2)
values2 = [3, 4]
update_values(values1, values2)

print(values1, values2)
