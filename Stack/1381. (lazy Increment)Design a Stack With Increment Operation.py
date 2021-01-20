#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 1381. (lazy Increment)Design a Stack With Increment Operation.py
@Time    : 12/2/2020 10:27 AM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class CustomStack:
    """
    Stack + lazy increment
    lazy increment is actually another stack to asisst increment in large data, the increment val will be added only pop()

    """

    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)