#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 209. Minimum Size Subarray Sum.py
@Time    : 11/26/2020 9:33 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        To get the shortest subarray whose sum is more than target value, we need a start and end. Once nums[start:end] is more than target, is pointless to extent more end cuz all elements are positive,
        people should extend start to try other subarray which could obtain shorter length
        """
        target_length = len(nums) + 1  # the length of subarray having shortest length
        start = sum_subarray = 0
        for end in range(len(nums)):
            sum_subarray += nums[end]
            while sum_subarray >= s and start <= end:
                target_length = min(target_length, end - start + 1)
                sum_subarray -= nums[start]
                start += 1
        if target_length == len(nums) + 1:
            return 0
        else:
            return target_length
