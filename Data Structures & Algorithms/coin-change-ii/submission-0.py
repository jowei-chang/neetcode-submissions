class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(len(coins)+1) for _ in range(amount+1)]
        dp[0] = [1]*(len(coins)+1)

        for aa in range(1, amount+1):
            for cidx in range(len(coins)):
                dp[aa][cidx+1] = dp[aa][cidx]
                if aa-coins[cidx]>=0:
                    dp[aa][cidx+1] += dp[aa-coins[cidx]][cidx+1]
                    
        return dp[amount][len(coins)]