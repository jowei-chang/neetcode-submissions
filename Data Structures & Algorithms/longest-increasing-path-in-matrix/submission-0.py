class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = {}         # (r,c): longest increasing path

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r,c)]
            path = 0
            # move up
            if r>0 and matrix[r-1][c]>matrix[r][c]:
                path = max(path, dfs(r-1,c)+1)
            # move down
            if r<R-1 and matrix[r+1][c]>matrix[r][c]:
                path = max(path, dfs(r+1,c)+1)
            # move left
            if c>0 and matrix[r][c-1]>matrix[r][c]:
                path = max(path, dfs(r,c-1)+1)
            # move right
            if c<C-1 and matrix[r][c+1]>matrix[r][c]:
                path = max(path, dfs(r,c+1)+1)
            dp[(r,c)] = path
            return dp[(r,c)]

        return max(dfs(r,c)+1 for r in range(R) for c in range(C))