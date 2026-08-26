"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visted = set()
        nodes = {1: Node(1)}
        queue = [node]
        while queue:
            nd = queue.pop()
            visted.add(nd.val)
            for nei in nd.neighbors:
                if nei.val not in nodes:
                    nodes[nei.val] = Node(nei.val)
                nodes[nd.val].neighbors.append(nodes[nei.val])
                if nei.val not in visted and nei not in queue:
                    queue.append(nei)
        return nodes[1]