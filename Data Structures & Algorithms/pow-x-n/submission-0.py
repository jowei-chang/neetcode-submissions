class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mySubPow(x, n):
            if n==0: return 1
            if n==1:
                return x
            elif n%2==0:
                return mySubPow(x*x, n//2)
            else:
                return mySubPow(x*x, n//2)*x
        
        if n<0:
            ans = 1.0/mySubPow(x, abs(n))
        else:
            ans = mySubPow(x, n)
        return ans