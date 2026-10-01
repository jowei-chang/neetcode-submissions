class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [collections.defaultdict(int) for _ in range(N+1)]
        dp[0][0] = 1    # (0 element, 0 sum): 1 way
        for idx in range(N):
            for acc, count in dp[idx].items():
                dp[idx+1][acc-nums[idx]] += count
                dp[idx+1][acc+nums[idx]] += count
        return dp[N][target]