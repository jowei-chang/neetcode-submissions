class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1]+nums+[1]
        # dp[ii][jj] means maxCoins(nums[ii:jj+1])
        dp = [[0]*(N+2) for _ in range(N+2)] 

        # ll: length, ii: left edge, jj: right edge, kk: midle point
        for ll in range(1, N+1):     # l: jj-ii=l
            for ii in range(1, N-ll+2):     
                jj = ii+ll-1
                for kk in range(ii, jj+1):
                    dp[ii][jj] = max(dp[ii][jj], dp[ii][kk-1]+nums[ii-1]*nums[kk]*nums[jj+1]+dp[kk+1][jj])
        return dp[1][N]