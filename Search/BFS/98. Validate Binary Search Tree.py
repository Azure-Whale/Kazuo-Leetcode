# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
"""
Iterate this BT using BST, for each node, make sure it will be larger than the lower limit
larger than the upper limit

What's the lower/upper limit?
it comes from previous nodes
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        stack = deque()
        
        if root:
            stack.append((root, -math.inf, math.inf)) # node val, lower limit, high limit
        else:
            return False
        
        while stack:
            Node,lower,higher = stack.popleft()
            if not Node:
                continue
            if Node.val <= lower or Node.val >= higher:
                return False
            
            stack.append((Node.left,lower,Node.val))
            stack.append((Node.right,Node.val,higher))
        
        return True
            