#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 57. Insert Interval.py
@Time    : 10/29/2020 6:35 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        The problem here is to get understand two things:
        1. what's the new range for the one you are inserting
        2. when should u insert the new one
        """
        #. if None, return
        if not newInterval:
            return intervals
        new_intervals = []
        #  init the range for the one you are inserting
        new_start,new_end = newInterval
        #. set a flag to help you insert
        Inserted = False

        #  This is not a if-elif structure, we can do this cuz there is no overlaping, each case can ba triggered independently
        for interval in intervals:
            # if the interval is before the new one, insert it directly
            if interval[1]<new_start:
                new_intervals.append(interval)
            # if the interval contains the start of new one, update the new one starting
            if interval[0]<=new_start<=interval[1]:
                new_start = interval[0]
            # if the interval is included by the new one, omit it
            if interval[0]>new_start and interval[1]<new_end:
                continue
            # if the interval contains the end of the new one, update the new one ending
            if interval[0]<=new_end<=interval[1]:
                new_end = interval[1]

            if new_end<interval[0]:
                if not Inserted:
                    new_intervals.append([new_start,new_end])
                    Inserted = True
                new_intervals.append(interval)
        if not Inserted:  #  if we don't update either start or end, the new interval will still be added if it haven't been added yet
            new_intervals.append([new_start,new_end])
        return new_intervals