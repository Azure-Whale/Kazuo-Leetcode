#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 15. 3Sum.py
@Time    : 1/3/2021 3:45 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The main idea here is keep that you shall not repeat on same elements, comapre the current one with the previous one and see if there is a difference
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                # if the smallest is more than 0, then the bigger one cannot be negative
                break
            if i == 0 or nums[i - 1] != nums[i]: # the first one should be unique, for each unqiue first, find all match pairs to contribute to the trumplet
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0 or (lo > i + 1 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1