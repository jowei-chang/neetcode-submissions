class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+1)
        for ii in range(2, n+1):
            dp[ii] = dp[ii-1]+dp[ii-2]
        return dp[-1]