class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(rr, cc):
            if rr<0 or rr==self.R or cc<0 or cc==self.C or self.grid[rr][cc]=='0':
                return 
            
            self.grid[rr][cc] = "0"
            bfs(rr-1,cc)
            bfs(rr+1,cc)
            bfs(rr,cc-1)
            bfs(rr,cc+1)

        n_island = 0
        self.R, self.C = len(grid), len(grid[0])
        self.grid = grid
        for rr in range(self.R):
            for cc in range(self.C):
                if grid[rr][cc]=="1":
                    n_island += 1
                    bfs(rr, cc)
        return n_island