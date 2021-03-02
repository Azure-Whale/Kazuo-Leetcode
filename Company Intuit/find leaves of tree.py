#https://leetcode.com/problems/find-leaves-of-binary-tree/
# double O(n) DFS + store all nodes in the list
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def DFS(root):
            if not root:
                return -1
            
            height = max(DFS(root.left),DFS(root.right)) + 1
            if height >= len(ans):
                ans.append([])
            ans[height].append(root.val)
            
            return height
        DFS(root)
        return ans