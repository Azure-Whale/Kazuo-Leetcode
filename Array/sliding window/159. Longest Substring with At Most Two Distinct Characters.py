#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 159. Longest Substring with At Most Two Distinct Characters.py
@Time    : 1/23/2021 2:19 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # left - start of the substring
        # right - end of the substring
        l = 0
        r = 1
        last = 0
        max_len = 0
        curr_sub = set()
        start = -1
        for i in range(len(s)):
            if not curr_sub:
                curr_sub.add(s[i])
                l = i
            if len(curr_sub) == 1:
                s[i] != s[l]
                curr_sub.add(s[i])
                r = i
                last = i
                start = i + 1
        if len(curr_sub) < 2 or start == len(s):
            return len(s)
        for i in range(start, len(s)):
            if s[i] in curr_sub:
                if s[i] != s[r]:
                    last = i
                r += 1
            if s[i] not in curr_sub:
                max_len = max(max_len, r - l + 1)
                curr_sub = {s[r], s[i]}
                l = last
                last = i
                r = i
            if (i == len(s) - 1):
                max_len = max(max_len, r - l + 1)

        return max_len

#         curr_max = 0
#         substring_records = [None,0,None,0,None,0] # first char, start_place of ...
#         for i in range(len(s)):
#             # init the substring record
#             if not substring_records[0]:
#                 substring_records[0] = s[i]
#                 substring_records[1] = i
#             if substring_records[0] and not substring_records[2]:
#                 substring_records[2] = substring_records[4] = s[i]
#                 substring_records[3] = substring_records[5] = i
#             # encounter new char and change the substring

#             if substring_records[2] and s[i]!=substring_records[2] and s[i]!=substring_records[0]:
#                 # record current length
#                 substring_legnth = ((i-1) -substring_records[1] + 1)
#                 # update the max if max is smaller than the current length
#                 if curr_max < substring_legnth:
#                     curr_max = substring_legnth
#                 # update the substring
#                 substring_records[0] = substring_records[2]
#                 substring_records[1] = substring_records[3]
#                 substring_records[2] = s[i]
#                 substring_records[3] = i
#             if i == len(s) - 1:
#                 # substring?
#                 if substring_records[0] and substring_records[2]:
#                     substring_legnth = ((i-1) -substring_records[1] + 1)
#                     if curr_max < substring_legnth:
#                         curr_max = substring_legnth
#         return curr_max
