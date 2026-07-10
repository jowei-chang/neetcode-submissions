# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if not node: 
                arr.append(None)
                return arr

            arr = dfs(node.left, arr)
            arr = dfs(node.right, arr)
            arr.append(node.val)
            return arr

        return dfs(p, [])==dfs(q, [])