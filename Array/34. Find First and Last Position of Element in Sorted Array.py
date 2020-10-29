#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 34. Find First and Last Position of Element in Sorted Array.py
@Time    : 10/29/2020 6:36 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binary_search_find_left(left, right, nums, target):
            while left <= right:
                mid = (left + right) // 2
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left  # we should return left cuz right = left -1 finally, and left finally reach the left

        def binary_search_find_right(left, right, nums, target):
            while left <= right:
                mid = (left + right) // 2
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right  # we should return right cuz left = right + 1 finally, and left finally reach the left

        left = binary_search_find_left(0, len(nums) - 1, nums, target)
        right = binary_search_find_right(0, len(nums) - 1, nums, target)
        print(left, right)
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]