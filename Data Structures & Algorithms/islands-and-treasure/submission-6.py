class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        R, C = len(grid), len(grid[0])
        for rr in range(R):
            for cc in range(C):
                if grid[rr][cc]==0:
                    queue.append((rr,cc))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r, c = queue.pop(0)
            for dr, dc in directions:
                rr, cc = r+dr, c+dc
                if 0<=rr<R and 0<=cc<C and grid[rr][cc]==2147483647:
                    grid[rr][cc] = grid[r][c]+1
                    queue.append((rr,cc))