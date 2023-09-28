"""
    05_using_pathlib.py

    The following code shows how to use the Path() object from the pathlib module.
    Numerous methods can replace the os module methods.

"""
from pathlib import Path

working_dir = Path('.')

if working_dir.exists():
    print(f'Absolute path for {working_dir} is {working_dir.resolve()}')
    print(f'The parent dir is: {working_dir.parent}')

if working_dir.is_dir():    # check if the Path object is a directory
    print()
    print('Get all contents (must use iteratively)')
    for p in working_dir.glob('*'):
        print('--> ', p)

print()
print('Get all contents recursively as Path objects (incl. all subdirs)')
for p in working_dir.glob('**/*'):
    print('--> ', p)

print()
print('Getting only files (as Path objects)...')
files_only = [p for p in working_dir.iterdir() if p.is_file()]
print([p.name for p in files_only])

print()
print(f'Reading part of first text file:')
print(files_only[0].read_text(encoding='utf-8')[:140])