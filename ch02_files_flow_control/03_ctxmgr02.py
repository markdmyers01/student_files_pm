"""

    03_ctxmgr02.py
    Context Manager life cycle.

"""
class MyContextManager(object):
    def __enter__(self):
        print('in enter')
        return 'foo'

    def __exit__(self, typ, value, traceback):
        print('in exit')


with MyContextManager() as obj:
    print(obj)
