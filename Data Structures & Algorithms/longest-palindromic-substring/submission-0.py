class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        res = ""
        n_res = 0
        for ii in range(N):
            ss=ee=ii
            while ss>=0 and ee<N and s[ss]==s[ee]:
                ss-=1
                ee+=1
            if ee-ss-1>n_res:
                n_res = ee-ss-1
                res = s[ss+1:ee]
            ss=ii
            ee=ii+1
            while ss>=0 and ee<N and s[ss]==s[ee]:
                ss-=1
                ee+=1
            if ee-ss-1>n_res:
                n_res = ee-ss-1
                res = s[ss+1:ee]
        return res