# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower=None, upper=None):
            if lower is not None:
                if node.val <= lower:
                    return False
            if upper is not None:
                if node.val >= upper:
                    return False
            if node.left:
                is_valid = dfs(node.left, lower, node.val)
                if is_valid is False:
                    return False
            if node.right:
                is_valid = dfs(node.right, node.val, upper)
                if is_valid is False:
                    return False
            return True

        return dfs(root)