#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 228. Summary Ranges.py
@Time    : 10/29/2020 6:37 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        p = 0

        def helper(lower, upper):
            if lower == upper:
                return f'{lower}'
            else:
                return f'{lower}->{upper}'

        if not nums:
            return None
        if len(nums) == 1:
            return [helper(nums[0], nums[0])]
        else:
            start = last = nums[0]
            end = None
            for i in range(len(nums)):
                end = nums[i]
                if end - last > 1:
                    res.append(helper(start, last))
                    start = end
                last = end
                if i == len(nums) - 1:
                    res.append(helper(start, end))
        return res
