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


for f in os.listdir('.'):
    if f.endswith('.py'):
        shutil.copy(f, './temp')

shutil.copytree('./temp', './temp/temp2')
shutil.move('./temp/temp2', '.')
