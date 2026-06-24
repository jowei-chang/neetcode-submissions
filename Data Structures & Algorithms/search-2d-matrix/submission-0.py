class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        up_r, down_r = 0, row-1
        left_c, right_c = 0, col-1

        while up_r<=down_r:
            mid_r = (up_r+down_r)//2
            if target>matrix[mid_r][-1]:
                up_r = mid_r+1
            elif target<matrix[mid_r][0]:
                down_r = mid_r-1
            else:
                while left_c <= right_c:
                    mid_c = (left_c+right_c)//2
                    if target>matrix[mid_r][mid_c]:
                        left_c = mid_c+1
                    elif target<matrix[mid_r][mid_c]:
                        right_c = mid_c-1
                    else:
                        return True
                break
        return False