class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}             # (p1, p2): True/False  (s3 can be built)
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1+n2!=n3: return False

        def dfs(p1,p2):
            if p1+p2==n3: return True
            if (p1,p2) in dp: return dp[(p1,p2)]
            if p1>n1: return False
            if p2>n2: return False
            flag = False
            if p1<n1 and s3[p1+p2]==s1[p1]:
                flag |= dfs(p1+1,p2)
            if p2<n2 and s3[p1+p2]==s2[p2]:
                flag |= dfs(p1,p2+1)
            dp[(p1,p2)] = flag
            return flag
        return dfs(0,0)