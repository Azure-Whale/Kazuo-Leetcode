#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 56. Merge Intervals.py
@Time    : 10/24/2020 10:32 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort is the key for the problem
        """
        intervals.sort(key=lambda x: x[0])  # The key point

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
