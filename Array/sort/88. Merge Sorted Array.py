#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 88. Merge Sorted Array.py
@Time    : 10/23/2020 11:41 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Attention: they are sorted arraries
        Since no more extra space are allowed, just compare usable part in nums1 and nums2. If there is remaining in
        nums2 after insertion, get it back to nums1
        """

        # m is the length of nums1, n is the length of nums2
        idx1 = m - 1
        idx2 = n - 1
        idx = m + n - 1

        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            idx -= 1
        # if there is a remaining for nums2
        nums1[:idx2 + 1] = nums2[:idx2 + 1]
