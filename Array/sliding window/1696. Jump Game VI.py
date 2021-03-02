#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 1696. Jump Game VI.py
@Time    : 1/23/2021 3:28 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque()
        # create a list to store window slide score
        max_scores = [0] * len(nums)
        max_scores[0] = nums[0]
        q.append(0)
        for i in range(1, len(nums)):
            # k steps before i is uesless
            while q and q[0] < i - k:
                q.popleft()
            # update max score, it is got from score(current step) + max(score that to need reach at previous k steps)
            max_scores[i] = nums[i] + nums[q[0]]
            while q and nums[q[0]] < nums[i]:
                q.popleft()
            q.append(i)

        # 0 1 2
        return max_scores[-1]

