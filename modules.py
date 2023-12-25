# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date # import only specific constructor from module
from time import time

today1 = datetime.date.today()
today2 = date.today()
print(today1)
print(today2)
print('----------------------------')

timestamp2 = time()
print(timestamp2)
print('----------------------------')
