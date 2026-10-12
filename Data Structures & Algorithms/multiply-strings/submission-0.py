class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]: return "0"
        ans = [0]*(len(num1)+len(num2))
        order1 = 0
        for s2 in num2[::-1]:
            jj = ord(s2)-ord("0")
            order2 = order1
            for s1 in num1[::-1]:
                ii = ord(s1)-ord("0")
                nn = jj*ii
                order = 0
                while nn>0:
                    nn += ans[order2+order]
                    ans[order2+order] = nn%10
                    nn//=10
                    order+=1
                order2+=1
            order1+=1
        res = ""
        flag = False
        for ii, ss in enumerate(ans[::-1]):
            if ss!=0:
                flag = True
            if flag:
                res+=str(ss)
        return res