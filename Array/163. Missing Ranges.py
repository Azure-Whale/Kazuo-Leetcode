#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 163. Missing Ranges.py
@Time    : 10/24/2020 10:31 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        To detect whether there is a missing range or not, we can detect whether the diff between last ele and current ele is more than 1 or not,
        if it doesn, then there is a missing, add last + 1, ele -1 into the range.
        However, since the start and end of the nums dont always fit in the lower and upper, then two case needed to be addressed
        The first ele should be lower - 1, assume our last element is the one before upper, so it would be okay if nums[0] is upper or upper + 1
        If the nums[-1]!=last, add the remaining part to the missing range
        """
        last = lower - 1
        connection_sign = '->'
        missing_ranges = []

        if not nums:
            if lower != upper:
                s = str(lower) + connection_sign + str(upper)
            else:
                s = str(lower)
            missing_ranges.append(s)

        for i in range(len(nums)):
            if nums[i] - last > 1:
                if last + 1 != nums[i] - 1:
                    s = str(last + 1) + connection_sign + str(nums[i] - 1)
                else:
                    s = str(last + 1)
                missing_ranges.append(s)
            last = nums[i]

            if i == len(nums) - 1 and nums[-1] != upper:
                last = nums[i]

                if last + 1 != upper:
                    s = str(last + 1) + connection_sign + str(upper)
                else:
                    s = str(last + 1)
                missing_ranges.append(s)
        return missing_ranges
