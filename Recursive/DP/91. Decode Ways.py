#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 91. Decode Ways.py
@Time    : 1/3/2021 1:53 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def __init__(self):
        self.memo = {}

    def recursive_with_memo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s) - 1:
            return 1

        # Memoization is needed since we might encounter the same sub-string.
        if index in self.memo:
            return self.memo[index]

        ans = self.recursive_with_memo(index + 1, s) \
              + (self.recursive_with_memo(index + 2, s) if (int(s[
                                                                index: index + 2]) <= 26) else 0)  # if the range doesn't exist in the list, it will return [] instead of an error

        # Save for memoization
        self.memo[index] = ans

        return ans

    def numDecodings(self, s: str) -> int:
        return self.recursive_with_memo(0, s)
