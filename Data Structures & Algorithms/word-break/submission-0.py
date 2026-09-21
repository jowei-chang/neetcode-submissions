class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False]*N
        for ii in range(N-1, -1, -1):
            for ww in wordDict:
                if ii+len(ww)<=N and ww==s[ii:ii+len(ww)]:
                    if ii+len(ww)==N or dp[ii+len(ww)]:
                        dp[ii] = True
                        break
        return dp[0]