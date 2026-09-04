class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        adj = [[] for _ in range(n)]
        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)
        q = [0]
        visited = set()
        visited.add(0)
        while q:
            node = q.pop(0)
            for nd in adj[node]:
                if nd not in visited:
                    visited.add(nd)
                    q.append(nd)
        return len(visited)==n