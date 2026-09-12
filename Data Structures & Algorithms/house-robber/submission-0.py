class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0]*N for _ in range(2)]  # row 0: rob, row1: no rob
        dp[0][0] = nums[0]
        for ii, nn in enumerate(nums):
            dp[0][ii] = nums[ii]+dp[1][ii-1]
            dp[1][ii] = max(dp[0][ii-1], dp[1][ii-1])
        return max(dp[0][N-1], dp[1][N-1])