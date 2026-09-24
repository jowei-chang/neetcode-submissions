class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2147483647    # end with 7
        MIN_INT = -2147483648   # end with -8
        MAX_mod = MAX_INT%10
        MIN_mod = int(math.fmod(MIN_INT,10))
        MAX_div = MAX_INT//10
        MIN_div = int(MIN_INT/10)
        res = 0
        while x:
            rem = int(math.fmod(x,10))      # python worng: -1%10 = 9
            x = int(x/10)                   # python worng: -1//10 = -1
            # over MAX_INT (>2147483647)
            if (res>MAX_div or (res==MAX_div and rem>MAX_mod)):
                return 0
            # below MIN_INT (<-2147483648)
            if (res<MIN_div or (res==MIN_div and rem<MIN_mod)):
                return 0
            res = res*10 + rem
        
        print("end")
        return res