"""

       Mini-task 1 - f-strings and slicing

       Task: Display the following output given the string below:
            OS: Windows NT 10.0

"""
import platform
import sys

ua = 'Mozilla/5.0 (Windows-2012 Server R2)'

print(platform.platform())
print(sys.platform)

print(ua.split("("))
print('OS: ' + (ua.split("(")[1]).split(")")[0])

print('My simple version:')
start = ua.find('(') + 1
end = ua.find(')')
print(start, end)
print('OS: ' + ua[start: end])

print('\nMore thoughtful version:')
start = ua.find('(')
end = ua.find(')')

if start != -1 and end != -1:
    print('OS: ' + ua[start + 1: end])
