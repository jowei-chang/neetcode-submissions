class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtracking(buf, acc, idx):
            for ii in range(idx, self.N):
                if acc + self.candidates[ii] == self.target:
                    self.ans.append(buf+[self.candidates[ii]])
                elif acc + self.candidates[ii] < self.target:
                    backtracking(buf+[self.candidates[ii]], acc+self.candidates[ii], ii)

        self.ans = []
        self.candidates = nums
        self.target = target
        self.N = len(nums)

        backtracking([], 0, 0)
        return self.ans