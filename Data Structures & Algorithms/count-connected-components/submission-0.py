class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)

        res = 0
        visited = [0]*n
        for ii in range(n):
            if visited[ii]==0:
                visited[ii] = 1
                res += 1
                q = [ii]
                while q:
                    idx = q.pop(0)
                    for jj in adj[idx]:
                        if visited[jj]==0:
                            visited[jj]=1
                            q.append(jj)
        return res