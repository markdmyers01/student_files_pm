"""

    05_diff_util.py
    Use of context managers (and a module) to compare two files.

"""
file1, file2 = 'sample1.txt', 'sample2.txt'

with open(file1, encoding='utf-8') as f1, open(file2, encoding='utf-8') as f2:
    for line_num, (line1, line2) in enumerate(zip(f1, f2), 1):
        line1 = line1.strip()
        line2 = line2.strip()
        if line1 != line2:
            print(f'Diff line: {line_num:<10}|{line1:40}|{line2:40}|')


# Using the Python standard library module...
from difflib import Differ
diff = Differ().compare(open('sample1.txt', encoding='utf-8').readlines(),
                        open('sample2.txt', encoding='utf-8').readlines())
print(*diff)
