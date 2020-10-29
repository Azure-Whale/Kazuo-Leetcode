#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 53. Maxium Subarray.py
@Time    : 10/21/2020 10:16 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


"""
Most used approach:
The idea here is to achieve global optimal solution from every local optimal solution
To get a maxium subarray, two things need to be get, the start and end of this subarray
Iterate the array:
Suppose we start from the index 0, and iterate following elements to see where we should end. B
But How to get to know where is the best the place to end, there are two cases:
1. The start need to be reset
2. Note the ending index make the subarray biggest so far and till you iterate the end of the whole array

Method 2 is easy to understand, just assume you have already get the start of your desirable subarray
Method 1, however, the only case there is a reason you should change your start is that the end is bigger than previous
extend. Since the end is bigger than previous sum, why not start from itself? So we update our start and then continue
the iteration till we found the optimal solution.
"""
#这个solution会返回start 和 end,只求sum的话不需要
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sofar = max_sofar = nums[0]
        if not nums:
            return None
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i -1]
            curr_sofar = nums[i]
            max_sofar = max(max_sofar, curr_sofar)
        return max_sofar

