#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 153. Find Minimum in Rotated Sorted Array.py
@Time    : 11/26/2020 10:01 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        You can search either from left to right, or the opposite. it's easy
        Once you found an element which doesn't follow the trend, that's where the max/min lies
        """
        ans = None
        if len(nums)<=1:
            return nums[0]
        for i in range(len(nums)-1,-1,-1):
            if ans==None:
                ans = nums[i]
                continue
            ans = min(ans,nums[i])
            if nums[i]>ans:
                break
        return ans