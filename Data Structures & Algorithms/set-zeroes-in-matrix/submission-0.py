class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_r = set()
        zero_c = set()
        R, C = len(matrix), len(matrix[0])
        for rr in range(R):
            for cc in range(C):
                if matrix[rr][cc]==0:
                    zero_r.add(rr)
                    zero_c.add(cc)
        for rr in zero_r:
            for cc in range(C):
                matrix[rr][cc] = 0

        for cc in zero_c:
            for rr in range(R):
                matrix[rr][cc] = 0