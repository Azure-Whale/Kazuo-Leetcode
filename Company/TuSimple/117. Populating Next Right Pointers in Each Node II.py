"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
"""
The problem aims to add cross level linkage, using BFS then you can get nodes in each level in an order that nodes goes from the most left to the most right, link these nodes according to the order for nodes in each level, and you will get correct tree afterwards.
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        temp = deque([root])
        ans = [root.val]
        while temp:
            ans.append('#')
            stack = temp
            temp = deque()
            while stack:
                node = stack.popleft()
                if node.left:
                    temp.append(node.left)
                    ans.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    ans.append(node.right.val)
            for i in range(len(temp)-1):
                temp[i].next =  temp[i+1]
        return root
                
            
            
        