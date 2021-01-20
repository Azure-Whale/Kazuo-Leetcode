#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 1588. Sum of All Odd Length Subarrays.py
@Time    : 11/18/2020 10:41 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

class Solution:
    """
    Set a window to iterate this array with different sizes

    """
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        add_up = 0
        for window_size in range(1,len(arr)+1,2):
            for i in range(len(arr)-window_size+1): # the iterate times should plus 1
                window_start = i
                window_end = window_start + window_size
                add_up += sum(arr[window_start:window_end])
        return add_up