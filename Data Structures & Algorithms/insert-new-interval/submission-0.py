class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        xn, yn = newInterval
        N = len(intervals)
        if yn <= intervals[0][1]:
            if yn<intervals[0][0]:
                return [newInterval]+intervals
            else:
                intervals[0][0] = min(xn, intervals[0][0])
                return intervals
        # merge last
        if xn >= intervals[-1][0]:
            if xn>intervals[-1][1]:
                return intervals+[newInterval]
            else:
                intervals[-1][1] = max(yn, intervals[-1][1])
                return intervals
        # merge middle
        res = []
        merge = []
        x, y = xn, yn
        for ii, (xi, yi) in enumerate(intervals):
            if yi<xn:
                res.append([xi, yi])
            elif xi<=xn<=yi or xi<=yn<=yi or (xi<=xn and yi>=yn) or (xn<=xi and yn>=yi):
                merge.append(ii)
                x = min(x, xi)
                y = max(y, yi)
                if ii==N-1:
                    res.append([x,y])
            elif xi>yn:
                res.append([x,y])
                res += intervals[ii:]
                break
        return res