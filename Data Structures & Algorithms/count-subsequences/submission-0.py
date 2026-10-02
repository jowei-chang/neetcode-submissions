class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        Ns = len(s)
        Nt = len(t)
        dp = [[0]*(Ns+1) for _ in range(Nt+1)]
        for ii in range(Ns+1):
            dp[0][ii] = 1
        for ii in range(Nt):
            for jj in range(Ns):
                if s[jj]==t[ii]:
                    dp[ii+1][jj+1] = dp[ii+1][jj]+dp[ii][jj]
                else:
                    dp[ii+1][jj+1] = dp[ii+1][jj]
        return dp[Nt][Ns]