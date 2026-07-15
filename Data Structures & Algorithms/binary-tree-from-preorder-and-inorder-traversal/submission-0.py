# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left>right: return None
            root = TreeNode(self.preorder[self.preidx])
            mid = self.idx[self.preorder[self.preidx]]
            self.preidx += 1
            root.left = build(left, mid-1)
            root.right = build(mid+1, right)
            return root

        self.idx = {}
        self.preorder = preorder
        self.inorder = inorder
        self.preidx = 0
        N = 0
        for nn in inorder:
            self.idx[nn] = N
            N += 1
        return build(0, N-1)