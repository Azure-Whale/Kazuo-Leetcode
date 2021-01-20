#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 70. Climbing Stairs.py
@Time    : 1/3/2021 2:35 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
"""


class Solution:
    # First, you only need to get the number of possible solutions The potential ways to get i-th step is the sum of
    # (potential ways reaching i - 1 step) and (potential ways reaching i - 2 step)

    def climbStairs(self, n: int) -> int:
        ans = [1, 2]
        for i in range(2, n):
            ans.append(
                ans[i - 1] + ans[i - 2]
            )

        return ans[n - 1]

    # Following approach use recursive to iterate each possible ways, it could output all possible path,
    # tho not a wise idea to get only the number of possible ways

    '''def __init__(self):
        self.n = None
        self.ways = None
    def recursive(self,cur_steps,len_step,n):
            cur_steps +=len_step
            if cur_steps == n:
                self.ways +=1
                return
            else:
                self.recursive(cur_steps,1,n)
                if cur_steps<n-1:
                     self.recursive(cur_steps,2,n)


    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        self.ways = 0        
        self.recursive(0,1,n)
        self.recursive(0,2,n)
        return self.ways'''