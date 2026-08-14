class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = [[] for _ in range(2**N)]
        for ii in range(2**N):
            num = bin(ii)[2:].zfill(N)
            for jj in range(N):
                if num[jj]=='1':
                    ans[ii].append(nums[jj])
        return ans