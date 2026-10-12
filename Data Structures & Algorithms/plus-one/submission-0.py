class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        carry = 1
        res = []
        for ii in range(N):
            n=digits[-ii-1]
            if carry==1:
                n += carry
                carry = n//10
                n %= 10 
            res.append(n)
        if carry==1:
            res.append(carry)
        return res[::-1]