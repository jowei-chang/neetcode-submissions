class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai = len(a) - 1
        bi = len(b) - 1
        res = ""
        carry = 0
        while ai>=0 or bi>=0 or carry:
            if ai>=0:
                carry+=int(a[ai])
                ai-=1
            if bi>=0:
                carry+=int(b[bi])
                bi-=1
            res = str(carry%2)+res
            carry//=2
        return res