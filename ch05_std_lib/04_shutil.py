"""
    04_shutil.py

    Before running:
                        ch05_std_lib
                              |
                              |__temp (empty)

    After running:
                        ch05_std_lib
                              |
                              |__temp (with 9 files)
                              |
                              |_ temp2 (with 9 files)
"""
import os
import shutil

temp_temp2 = './temp/temp2'
temp2 = './temp2'
temp = './temp'
dirs = [temp_temp2, temp2, temp]


def check_permissions(filepath):
    '''Checks the permissions of the specified file'''
    try:
        stat_info = os.stat(filepath)
        return oct(stat_info.st_mode)[-3:] # Print last 3 digits of octal representation of st_mode
    except IOError as e:
        print(os.strerror(e)) # Print the error message from errno as a string



for dir in dirs:
    if os.path.exists(dir):
        print(f'Directory permissions: {check_permissions(dir)} for {dir}')
        shutil.rmtree(dir)

os.mkdir(temp)

for f in os.listdir('.'):
    if f.endswith('.py'):
        shutil.copy(f, temp)

shutil.copytree(temp, temp_temp2)

shutil.move(temp_temp2, '.')
