class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        visited = set()
        while res>=5 and res not in visited:
            visited.add(res)
            acc=0
            while res!=0:
                acc+=(res%10)**2
                res //= 10
            res=acc
        if res==1: return True
        return False