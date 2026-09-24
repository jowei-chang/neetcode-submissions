class Solution:
    def hammingWeight(self, n: int) -> int:
        n1 = 0
        while n:
            n1 += n&1
            n//=2
        return n1