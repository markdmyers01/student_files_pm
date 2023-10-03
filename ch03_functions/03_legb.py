"""

    03_legb.py
    Understanding variable scope and visibility.

"""
x = 10
list1 = [1, 2, 3]


def f1():
    # y = x *2
    # print(x)
    global x
    x *= 2
    print(x)
    y = x * 10
    list1.append(y)
    # print(y)

    # def f2():
    #     x = 30
    #     print(x)
    # f2()


f1()
print(x)
print(list1)
