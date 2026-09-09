class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]      # (elevation, x, y)
        visited = set()
        visited.add((0,0))
        while heap:
            h, r, c = heapq.heappop(heap)
            if r==R-1 and c==C-1:
                return h
            
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                rr, cc = r+dr, c+dc
                if 0<=rr<R and 0<=cc<C and (rr,cc) not in visited:
                    visited.add((rr,cc))
                    heapq.heappush(heap, (max(h, grid[rr][cc]), rr, cc))