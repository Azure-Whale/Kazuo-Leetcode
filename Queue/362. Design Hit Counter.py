#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 362. Design Hit Counter.py
@Time    : 1/16/2021 12:14 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_counter = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hit_counter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        while True:
            # remove the hit happened 300 sec ago
            if len(self.hit_counter) > 0:
                # compare the first hit and current query time, keep removing until the remaining elements only happened 300 sec before the query timestamp
                if (timestamp - self.hit_counter[0]) >= 300:
                    # remove the earliest hit
                    self.hit_counter.popleft()
                else:
                    break
            else:
                break

        return len(self.hit_counter)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)