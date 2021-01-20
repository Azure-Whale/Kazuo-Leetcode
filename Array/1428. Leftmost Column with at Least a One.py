#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 1428. Leftmost Column with at Least a One.py
@Time    : 11/15/2020 5:46 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    """
    Search from the top right, and only go left and down.
    """

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        if rows < 1 or cols < 1:
            return -1

        curr_row = 0
        curr_col = cols - 1
        while curr_row < rows and curr_col >= 0:
            if not binaryMatrix.get(curr_row, curr_col):
                curr_row += 1
            else:
                curr_col -= 1

        # If we never left the last column, it must have been all 0's.
        return curr_col + 1 if curr_col != cols - 1 else -1




