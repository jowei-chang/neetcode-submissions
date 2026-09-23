class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = {}
        for ii in range(m):
            table[(ii,0)] = 1
        for ii in range(n):
            table[(0,ii)] = 1
            
        for ii in range(1,m):
            for jj in range(1,n):
                table[(ii,jj)] = table[(ii-1,jj)] + table[(ii,jj-1)]
        return table[(m-1,n-1)]