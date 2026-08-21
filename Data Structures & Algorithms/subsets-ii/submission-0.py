class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(buf, idx):
            if idx==self.N-1:
                if buf not in self.ans:
                    self.ans.append(buf)
                if buf+[self.nums[idx]] not in self.ans:
                    self.ans.append(buf+[self.nums[idx]])
                return
            
            backtracking(buf,idx+1)
            backtracking(buf+[self.nums[idx]],idx+1)

        nums.sort()
        self.nums = nums
        self.N = len(nums)
        self.ans = []
        backtracking([], 0)
        return self.ans