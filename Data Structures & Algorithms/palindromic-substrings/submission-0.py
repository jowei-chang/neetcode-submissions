class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        for ii in range(N):
            ss=ee=ii
            while ss>=0 and ee<N and s[ss]==s[ee]:
                ss-=1
                ee+=1
                res+=1
            ss=ii
            ee=ii+1
            while ss>=0 and ee<N and s[ss]==s[ee]:
                ss-=1
                ee+=1
                res+=1
        return res