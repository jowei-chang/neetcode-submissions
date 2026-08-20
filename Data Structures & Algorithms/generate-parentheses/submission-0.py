class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(buf, nL, nR):
            if nL==0 and nR==0:
                self.ans.append(buf)
                return 
            if nL>0:
                backtracking(buf+'(', nL-1, nR)
            if nR>nL:
                backtracking(buf+')', nL, nR-1)

        self.ans = []
        backtracking("", n, n)
        return self.ans