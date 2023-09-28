"""

    02_os_stat.py
    Getting a files statistics.

"""
import os
import time

stats = os.stat('02_os_stat.py')
print(stats)
print(stats.st_size)
print(stats.st_atime)
print(time.ctime(stats.st_atime))
print(time.strftime('%m-%d-%Y', time.localtime(stats.st_atime)))
