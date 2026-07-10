# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [None]
            arrL = dfs(node.left)
            arrR = dfs(node.right)

            return arrL+arrR+[node.val]

        def dfs_root(node):
            flag = False
            if not node:
                if [None] == self.arrSub:
                    flag = True
                return [None], flag
            arrL, flag1 = dfs_root(node.left)
            arrR, flag2 = dfs_root(node.right)

            arr = arrL+arrR+[node.val]
            if arr == self.arrSub:
                flag = True
            return arr, flag1 or flag2 or flag
        
        self.arrSub = dfs(subRoot)
        _, ans = dfs_root(root)
        return ans