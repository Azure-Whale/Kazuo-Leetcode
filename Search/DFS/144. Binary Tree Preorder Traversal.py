#https://leetcode.com/problems/binary-tree-preorder-traversal/

# Just keep that, inorder, preorder, postorder, and the in ore post indicates the order of root, left right doesn't change the order, same for the N-ary Tree
# Here in this question, pre-order = root, left, right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # root, left, right
        
        ans = []
        def DFS(root,ans):
            
            if not root:
                return
            
            ans.append(root.val)
            
            DFS(root.left,ans)
            DFS(root.right,ans)
        DFS(root,ans)
        return ans