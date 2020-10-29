#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : Two Sum.py
@Time    : 10/21/2020 10:15 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

class TwoSum(object):
    """
    Using Dict or Two pointer to help you, if you need Two pointer, you shall sort it firstly( O(nlongn))
    """
    def twoSum1(self, nums, target):
        nums = list(sorted(enumerate(nums), key=lambda x: x[1])) # It keeps the origin index but sort by current value
        left = 0
        right = len(nums) - 1
        while left < right:
            add_up = nums[left][1] + nums[right][1]
            if add_up == target:
                break
            elif add_up > target:
                right -= 1
            else:
                left += 1
        if left != right:
            return [nums[left][0], nums[right][0]]
        else:
            return None

    def twoSum3(self, nums, target):
        dict = {}
        for i, v in enumerate(nums):
            solution = target - v
            if solution in dict:
                return [i, dict[solution]]
            dict[v] = i