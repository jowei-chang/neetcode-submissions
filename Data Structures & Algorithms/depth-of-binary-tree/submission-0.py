# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth, max_depth):
            depth += 1
            if depth > max_depth:
                max_depth = depth
                
            if node.left:
                max_depth = dfs(node.left, depth, max_depth)
            if node.right:
                max_depth = dfs(node.right, depth, max_depth)

            return max_depth

        if root is None: return 0
        depth = 0
        max_depth = 0
        
        return dfs(root, depth, max_depth)