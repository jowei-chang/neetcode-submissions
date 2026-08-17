class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, N, res, vist, buf, n_level):
            if n_level == N:
                res.append(buf)
                return 

            for ii in range(N):
                if vist[ii] is False:
                    vist[ii] = True
                    backtracking(nums, N, res, vist, buf+[nums[ii]], n_level+1)
                    vist[ii] = False
        
        res = []
        N = len(nums)
        n_level = 0
        vist = [False]*N
        buf = []
        backtracking(nums, N, res, vist, buf, n_level)
        return res