class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for ii in range(N//2):
            for jj in range(ii, N-1-ii):
                # matrix[N-jj][ii] = tmp
                matrix[ii][jj], matrix[N-jj-1][ii] = matrix[N-jj-1][ii], matrix[ii][jj]

                # left-bottom => right-bottom
                matrix[N-jj-1][ii], matrix[N-ii-1][N-jj-1] = matrix[N-ii-1][N-jj-1], matrix[N-jj-1][ii]

                # right-bottom => right-top
                matrix[N-ii-1][N-jj-1], matrix[jj][N-ii-1] = matrix[jj][N-ii-1], matrix[N-ii-1][N-jj-1]