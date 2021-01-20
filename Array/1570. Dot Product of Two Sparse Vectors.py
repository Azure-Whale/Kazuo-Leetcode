#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 1570. Dot Product of Two Sparse Vectors.py
@Time    : 11/16/2020 11:35 AM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

"""
Sparse vectors is a vector consist of a lot of 0, if there is only dot computation purpose, we don't need to record
 them, only keep those within real value. Use Dictionary
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        if len(nums) <= 0:
            self.sparse_vec = None
        else:
            self.sparse_vec = dict()
            for index, number in enumerate(nums):
                if number:
                    self.sparse_vec[index] = number

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        target = 0
        if not self.sparse_vec or not vec.sparse_vec:
            return target
        set1 = set(self.sparse_vec.keys())
        set2 = set(vec.sparse_vec.keys())
        idxs = set1.intersection(set2)
        for index in idxs:
            target += self.sparse_vec[index] * vec.sparse_vec[index]
        return target

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)