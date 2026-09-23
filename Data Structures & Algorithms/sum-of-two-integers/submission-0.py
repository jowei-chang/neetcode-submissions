class Solution:
    def getSum(self, a: int, b: int) -> int:
        Mask = 0xFFF
        while (b&Mask) > 0:
            carry = (a&b)<<1
            a = a^b
            b = carry
        return (a&Mask) if b>0 else a