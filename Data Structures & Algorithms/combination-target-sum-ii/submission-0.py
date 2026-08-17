class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(buf, acc, idx):
            if acc==self.target:
                self.ans.append(buf)
            elif idx<=self.N-1 and acc+self.candidates[idx]<=self.target:
                if idx<=self.N-1:
                    backtracking(buf+[self.candidates[idx]], acc+self.candidates[idx], idx+1)
                    while idx<self.N-1 and self.candidates[idx]==self.candidates[idx+1]:
                        idx+=1
                    backtracking(buf, acc, idx+1)
        self.candidates = sorted(candidates)
        self.N = len(candidates)
        self.target = target
        self.ans = []
        backtracking([], 0, 0)
        return self.ans