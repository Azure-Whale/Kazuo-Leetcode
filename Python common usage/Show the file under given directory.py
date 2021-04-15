from os import listdir
from os.path import isfile,isdir
import os
# the test case is test_case folder itself

test_case = 'test_case'
ans = []

stack = []

stack.append('Python common usage/test_case')

for element in os.walk('Python common usage/test_case'):
    print(element)