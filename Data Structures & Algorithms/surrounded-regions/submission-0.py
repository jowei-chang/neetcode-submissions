class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        q = []
        for ii in range(R):
            if board[ii][0]=="O": q.append((ii,0))
            if board[ii][C-1]=="O": q.append((ii,C-1))
        for jj in range(C):
            if board[0][jj]=="O": q.append((0,jj))
            if board[R-1][jj]=="O": q.append((R-1,jj))

        visited = set()
        while q:
            r, c = q.pop(0)
            board[r][c] = "G"
            visited.add((r,c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                rr, cc = r+dr, c+dc
                if 0<=rr<R and 0<=cc<C and board[rr][cc]=="O" and (rr,cc) not in visited:
                    q.append((rr,cc))
        for ii in range(R):
            for jj in range(C):
                if board[ii][jj]=="G":
                    board[ii][jj]="O"
                elif board[ii][jj]=="O":
                    board[ii][jj]="X"