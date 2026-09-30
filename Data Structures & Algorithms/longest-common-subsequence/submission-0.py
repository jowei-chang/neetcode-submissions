class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1= len(text1)
        N2= len(text2)
        dp = [[0]*(N2+1) for _ in range(N1+1)]
        for ii in range(1, N1+1):
            for jj in range(1, N2+1):
                if text2[jj-1]==text1[ii-1]:
                    dp[ii][jj] = dp[ii-1][jj-1]+1
                else:
                    dp[ii][jj] = max(dp[ii-1][jj],dp[ii][jj-1])
        return dp[N1][N2]