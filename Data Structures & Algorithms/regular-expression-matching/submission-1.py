class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(sidx, pidx):
            # print("pidx: ", pidx, "sidx: ", sidx)
            if (sidx, pidx) in self.dp:
                return self.dp[(sidx, pidx)]
            # p match over and s match over
            if pidx>=self.Np:
                return sidx==self.Ns

            first = sidx<self.Ns and (p[pidx]=='.' or p[pidx]==s[sidx])
            # pattern: .* or a* ...
            if pidx+1<self.Np and p[pidx+1]=="*":
                # case1: '.*' or 'a*' = '' => jump a*
                # case2: 'a* => 'a', 'aa' or 'aaa'
                res = dfs(sidx, pidx+2) or (first and dfs(sidx+1, pidx))
            # single character
            else:
                res = first and dfs(sidx+1, pidx+1)
            self.dp[(sidx, pidx)] = res
            return res
        self.dp = {}
        self.Np = len(p)
        self.Ns = len(s)
        return dfs(0, 0)