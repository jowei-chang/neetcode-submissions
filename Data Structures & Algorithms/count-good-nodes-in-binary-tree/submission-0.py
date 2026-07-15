# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxmax, goodNode):
            if not node: return goodNode

            if node.val>=maxmax:
                goodNode += 1
                maxmax = node.val
            
            goodNode = dfs(node.left, maxmax, goodNode)
            goodNode = dfs(node.right, maxmax, goodNode)
            return goodNode
        return dfs(root, -10**5, 0)
