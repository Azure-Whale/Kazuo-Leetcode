#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 155. Min Stack.py
@Time    : 1/16/2021 6:31 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class MinStack:
    # it seems that this question doesn't allow you to use min() to record the minium value
    # therefore, we may record minium value for each node recording the min from the current
    # position to the buttom
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x: int) -> None:
        if not self.list:
            self.list.append((x, x))
        else:
            if self.list[-1][1] >= x:
                self.list.append((x, x))
            else:
                self.list.append((x, self.list[-1][1]))

    def pop(self) -> None:
        temp = self.list[-1][0]
        self.list = self.list[:-1]
        return temp

    def top(self) -> int:
        if not self.list:
            return None
        else:
            return self.list[-1][0]  # last item exist, return the value

    def getMin(self) -> int:
        if not self.list:
            return None
        else:
            return self.list[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()