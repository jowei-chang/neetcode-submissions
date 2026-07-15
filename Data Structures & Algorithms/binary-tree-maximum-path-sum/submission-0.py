# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return -1000

            left = dfs(node.left)
            right = dfs(node.right)
            
            maxmax = max(left+node.val, right+node.val, node.val)
            localMax = max(maxmax, left+node.val+right, left, right)
            if localMax > self.ans: 
                self.ans = localMax
            
            return maxmax
        self.ans = -1000
        dfs(root)
        
        return self.ans