class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(table, row, cols, diagR, diagL):
            if row==self.N:
                self.ans.append(["".join(r) for r in table])
                return 
            
            for cc in range(self.N):
                if cc in cols:
                    continue
                if cc-row in diagR:       # row-col==0 (正斜對角), row-col==1 (正斜對角往右一col)
                    continue
                if cc+row in diagL:
                    continue

                table[row][cc] = 'Q'
                backtracking(table, row+1, cols+[cc], diagR+[cc-row], diagL+[cc+row])
                table[row][cc] = '.'

        self.ans = []
        self.N = n
        table = [["."]*n for _ in range(n)]
        backtracking(table, 0, [], [], [])
        return self.ans