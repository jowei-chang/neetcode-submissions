class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)

        dp = [[0]*(N2+1) for _ in range(N1+1)]
        for ii in range(N1+1):
            dp[ii][0] = ii
        for ii in range(N2+1):
            dp[0][ii] = ii

        for ii in range(N1):
            for jj in range(N2):
                if word1[ii]==word2[jj]:             # case 1
                    dp[ii+1][jj+1] = dp[ii][jj]
                else:                                # case 2
                    dp[ii+1][jj+1] = min(dp[ii][jj+1], dp[ii+1][jj], dp[ii][jj]) + 1

        return dp[N1][N2]