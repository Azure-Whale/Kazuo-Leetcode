#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : Subarray Sum Equals K.py
@Time    : 10/22/2020 12:06 AM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

nums = [1, 2, 3, 4]
k = 5
sum_dict = {}
total = 0
for i in range(len(nums)):
    total += nums[i]
    sum_dict[total] = sum_dict.setdefault(total, 0) + 1
total = 0
for i in range(len(nums)-1):
    total += nums[(len(nums) - i - 1)]
    sum_dict[total] = sum_dict.setdefault(total, 0) + 1

print(sum_dict)
