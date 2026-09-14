class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0': return 0
        N = len(s)
        dp = [1]*(N+1)
        for ii in range(2, N+1):
            dp[ii] = dp[ii-1]+dp[ii-2]
        idx = 0
        prefix = ""
        res = 1
        while idx<N:
            prefix+=s[idx]
            if int(s[idx]) > 2 or idx == N-1 or int(s[idx]) == 0:
                if prefix=="0":
                    return 0
                if int(prefix[-2:])>26:
                    res*=(dp[len(prefix)-1])
                elif prefix[-1:]=="0":
                    res*=(dp[len(prefix)-2])
                else:
                    res*=dp[len(prefix)]
                prefix=""
            idx+=1
        return res