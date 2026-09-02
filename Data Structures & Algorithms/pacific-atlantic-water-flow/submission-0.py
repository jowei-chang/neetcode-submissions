class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, visited, pre_h):
            visited.add((r,c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                rr, cc = r+dr, c+dc
                if 0<=rr<self.R and 0<=cc<self.C and pre_h<=heights[rr][cc] and (rr,cc) not in visited:
                    dfs(rr,cc,visited,heights[rr][cc])

        self.R, self.C = len(heights), len(heights[0])
        pac, atl = set(), set()     # pac: left-top, alt: right-down

        for rr in range(self.R):
            dfs(rr,0,pac,heights[rr][0])
            dfs(rr,self.C-1,atl,heights[rr][self.C-1])

        for cc in range(self.C):
            dfs(0,cc,pac,heights[0][cc])
            dfs(self.R-1,cc,atl,heights[self.R-1][cc])
        res = []
        for r,c in pac & atl:
            res.append([r,c])
        return res