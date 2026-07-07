# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            L = dfs(node.left) if node.left else 0
            R = dfs(node.right) if node.right else 0
            self.ans = max(L+R, self.ans)
            return max(L,R)+1

        if not root: return 0
        self.ans = 0
        dfs(root)
        return self.ans