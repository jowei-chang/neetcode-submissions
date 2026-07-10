# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def bst(node, p, q):        # note:  p<q
            if node.val in [p.val, q.val] or (node.val > p.val and node.val < q.val):
                return node
            elif node.val > q.val:
                return bst(node.left, p, q)
            elif node.val < p.val:
                return bst(node.right, p, q)

        if p.val>q.val:
            ans = bst(root, q, p)
        else:
            ans = bst(root, p, q)
        return ans