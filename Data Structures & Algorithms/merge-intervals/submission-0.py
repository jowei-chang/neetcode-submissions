class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for xi, yi in intervals[1:]:
            if res[-1][1]>=xi:
                res[-1][1] = max(yi, res[-1][1])
            else:
                res.append([xi,yi])
        return res