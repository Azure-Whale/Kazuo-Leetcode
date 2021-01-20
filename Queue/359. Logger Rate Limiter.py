#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 359. Logger Rate Limiter.py
@Time    : 1/16/2021 12:13 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_timestamp = {}  # use a dict to record messge - timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        # if message haded existed in self.key_timestamp
        if message not in self.key_timestamp:
            self.key_timestamp[message] = timestamp
            return True
        else:
            if timestamp < (self.key_timestamp[message] + 10):
                return False
            else:
                self.key_timestamp[message] = timestamp
                return True
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)