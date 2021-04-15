"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        res = []

        def DFS(root, res):

            if not root:
                return None

            res.append(root.val)

            for child in root.children:
                DFS(child, res)

        DFS(root, res)
        return res