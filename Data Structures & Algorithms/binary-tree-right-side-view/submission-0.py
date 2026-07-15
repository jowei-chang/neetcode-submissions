# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, ans, depth):
            if not node: return ans

            if depth+1 > len(ans):
                ans.append(node.val)

            ans = dfs(node.right, ans, depth+1)
            ans = dfs(node.left, ans, depth+1)

            return ans
       
        return dfs(root, [], 0)