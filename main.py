'''
create a one package
untilities
calculator.py
greetings.py



main.py
import from untilities and use them



'''
from utilities.calculator import add
print(add(10,20))

from utilities.greeting import greet
print(greet("anand"))

import math
print(math.__name__)
print(math.__doc__)



import math

import sys
print(sys.path)

print(dir(math))


#pip-->python package manager

#1.sys
#multiple projects
#college_canteen--->numpy--1.0
#college_library-->numpy--2.0
#college_bus-->numpy-->1.5 version


#python virtual environment

#python -m venv env

