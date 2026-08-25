class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(rr, cc, area):
            if rr<0 or rr==self.R or cc<0 or cc==self.C or self.grid[rr][cc]==0:
                return area
            self.grid[rr][cc] = 0
            area+=1
            area = bfs(rr-1,cc, area)
            area = bfs(rr+1,cc, area)
            area = bfs(rr,cc-1, area)
            area = bfs(rr,cc+1, area)
            return area
            
        self.grid = grid
        self.R, self.C = len(grid), len(grid[0])

        maxArea = 0
        for rr in range(self.R):
            for cc in range(self.C):
                if grid[rr][cc]==1:
                    area = bfs(rr,cc, 0)
                    if area>maxArea:
                        maxArea = area
        return maxArea