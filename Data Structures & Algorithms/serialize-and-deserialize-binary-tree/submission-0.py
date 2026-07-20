# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs_encode(node):
            if not node:
                self.vals.append("- ")
                return 
            self.vals.append(str(node.val)+" ")
            dfs_encode(node.left)
            dfs_encode(node.right)
            
        self.vals = []
        dfs_encode(root)
        return "".join(self.vals)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs_decode():
            if self.lst_ss[self.idx] == '-':
                self.idx += 1
                return None
            else:
                node = TreeNode(int(self.lst_ss[self.idx]))
                self.idx += 1
                node.left = dfs_decode()
                node.right = dfs_decode()
                return node

        self.idx = 0
        self.lst_ss = data.split(" ")[:-1]
        root = dfs_decode()
        return root

