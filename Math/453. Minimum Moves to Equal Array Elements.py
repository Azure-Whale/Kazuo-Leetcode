#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 453. Minimum Moves to Equal Array Elements.py
@Time    : 11/18/2020 10:31 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

        To make the lowest equals to the highest,  the highest is actuall cnt
        for ele in nums:
            cnt += ele - min_ele

        """
        min_ele = min(nums)
        cnt = 0
        for ele in nums:
            cnt += ele - min_ele
        return cnt