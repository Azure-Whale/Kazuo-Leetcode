#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 215. Kth Largest Element in an Array.py
@Time    : 1/3/2021 3:51 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        This took O(nlogn), not that good
        '''
        # nums = sorted(nums)
        # return nums[-k]
        '''
        Better Method, always keep the biggest and k-th biggest list 
        This used heap to solve problem
        It sorted this list as a heap(Priority binary tree which parent<=children) and took nlogk
        '''
        return heapq.nlargest(k, nums)[-1]

        # The time complexity of adding an element in a heap of size k is \mathcal{O}(\log k)O(logk), and we do it N times that means \mathcal{O}(N \log k)O(Nlogk) time complexity for the algorithm.