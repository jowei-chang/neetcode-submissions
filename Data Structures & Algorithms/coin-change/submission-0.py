class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for ii in range(1, amount+1):
            for cc in coins:
                if ii-cc>=0:
                    dp[ii] = min(dp[ii], dp[ii-cc]+1)
        if dp[amount]>=amount+1:
            return -1
        return dp[amount]