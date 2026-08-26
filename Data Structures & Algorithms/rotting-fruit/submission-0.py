class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = []
        grids = [0]*R*C
        for rr in range(R):
            for cc in range(C):
                if grid[rr][cc]==1:
                    grids[rr*C+cc] = -1
                elif grid[rr][cc]==2:
                    grids[rr*C+cc] = 0
                    queue.append((rr,cc))
        if -1 not in grids: return 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r,c = queue.pop(0)
            for dr, dc in dirs:
                rr, cc =r+dr, c+dc
                if 0<=rr<R and 0<=cc<C and grids[rr*C+cc]==-1:
                    grids[rr*C+cc] = grids[r*C+c]+1
                    queue.append((rr,cc))
        if min(grids)<0:
            return -1
        return max(grids)