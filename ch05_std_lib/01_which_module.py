"""

    01_which_module.py
    Determining the physical location of a loaded module.

"""
import importlib
import sys


def which_mod(modules):
    for module in modules:
        if module in sys.builtin_module_names:
            print(f'{module} built in')
        else:
            try:
                module = importlib.import_module(module)
                location = module.__file__
                print(location)
            except (ValueError, ImportError):
                print(f'{module} not found', file=sys.stderr)


if len(sys.argv) > 1:                                               # accept names from command-line
    modules = sys.argv[1:]
else:                                                               # or read from input
    module_names = input('Module name(s) [separated by spaces]: ')
    modules = module_names.strip().split(' ')

if len(modules[0]) < 1:                                             # use defaults if nothing provided
    modules = ['os', 'sys', 'string', 'subprocess', 'foo']

which_mod(modules)
