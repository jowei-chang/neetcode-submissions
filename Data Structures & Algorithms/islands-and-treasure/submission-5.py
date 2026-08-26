class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        # Add all treasure chests (0) to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Perform BFS from all chests simultaneously
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds, water cells (-1), or already visited land cells
                if (0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    grid[nr][nc] == 2147483647): # INF value
                    
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))