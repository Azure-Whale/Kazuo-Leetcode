#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 1265. Print Immutable Linked List in Reverse.py
@Time    : 11/30/2020 9:27 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """
        It's actually a simple recursive problem
        """

        def helper(node):
            if node:
                helper(node.getNext())
                node.printValue()

        helper(head)