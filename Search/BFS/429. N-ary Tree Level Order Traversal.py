n_tree = [0,1,2,3,4,5,6]
"""
N-ary Tree means a tree has no more N children for a single root/parent , binary tree is 2-ary Tree

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
import heapq
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        # if empty tree
        if not root:
            return None

        current_level = []
        next_level = []
        current_level.append(root)
        ans = []
        
        while current_level:
            next_level = []
            temp = []
            for node in current_level:
                temp.append(node.val) # append element on the latest list, then you don;t need to append it on a temp list
                next_level.extend(node.children) # extend will append a list to current list with lower cost
            ans.append(temp)
            current_level = next_level
        return ans