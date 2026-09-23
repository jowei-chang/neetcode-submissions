class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for ii in range(n+1):
            ans[ii] = ans[ii>>1]+(ii&1)
        return ans