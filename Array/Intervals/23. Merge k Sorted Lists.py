#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 23. Merge k Sorted Lists.py
@Time    : 1/23/2021 5:18 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Put each ll in the pq, and the weight is measured by the current value of each ll,
        so each time you get value from the pq, it will get you the smallest value and its ll
        attention that, in the python3, Queue is queue, q.put() cannot insert ll in first two para, you should add a dummy q.put((ll.val,idx,curr_node)) such as idx
        """
        res = ListNode(None)
        head = res
        q = PriorityQueue()
        # init the PriorityQueue, generate a dummy idx so that you can use pq
        for idx,ll in enumerate(lists):
            if ll:
                curr_node = ll
                q.put((ll.val,idx,curr_node))
        while not q.empty():
            val,_,res.next = q.get()
            res = res.next
            if res.next:
                q.put((res.next.val,_,res.next))
        return head.next