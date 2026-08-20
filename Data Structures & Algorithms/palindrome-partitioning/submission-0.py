class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start, end):
            while start<end:
                if self.s[start]!=self.s[end]:
                    return False
                start+=1
                end-=1
            return True

        def backtracking(buf, start):
            if start == self.N:
                self.ans.append(buf)

            for end in range(start, self.N):
                if isPalindrome(start, end):
                    backtracking(buf+[self.s[start:end+1]], end+1)

        self.ans = []
        self.s = s
        self.N = len(s)
        backtracking([], 0)
        return self.ans