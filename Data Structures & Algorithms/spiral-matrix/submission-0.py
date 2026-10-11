class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        idx, n = 0, 0
        R, C = len(matrix), len(matrix[0])
        res = []
        visited = set()
        r, c = 0, 0
        dr, dc = dirs[idx]
        while n<R*C:
            res.append(matrix[r][c])
            visited.add((r,c))
            rr = r+dr
            cc = c+dc
            if (rr,cc) in visited or rr<0 or rr>=R or cc<0 or cc>=C:
                idx = (idx+1)%4
                dr, dc = dirs[idx]
                rr = r+dr
                cc = c+dc
            r = rr
            c = cc
            n+=1
        return res