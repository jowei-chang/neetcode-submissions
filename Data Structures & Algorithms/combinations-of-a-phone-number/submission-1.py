class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(buf, idx):
            if idx==self.N:
                self.ans.append(buf)
                return 

            for ss in self.table[self.digits[idx]]:
                backtracking(buf+ss, idx+1)

        self.table = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        self.ans = []
        self.N = len(digits)
        if self.N==0: return []
        self.digits = digits
        backtracking("", 0)
        return self.ans