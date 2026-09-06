class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(n):
            if n!=self.parent[n]:       # root node
                self.parent[n] = find(self.parent[n])
            return self.parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:      # has cycle
                return False

            if self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
            return True

        N = len(edges)
        self.parent = [ii for ii in range(N+1)]
        self.rank = [1]*(N+1)

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]