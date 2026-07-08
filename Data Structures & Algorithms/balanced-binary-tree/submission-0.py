# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return 0

            # left branch is unbalanced
            height_L = dfs(node.left)
            if height_L==-1: return -1
                
            # right branch is unbalanced
            height_R = dfs(node.right)
            if height_R==-1: return -1

            if abs(height_L-height_R) > 1:
                return -1
            
            return max(height_L, height_R)+1

        return dfs(root)!=-1