class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n_erase = 0
        last_ee = intervals[0][1]
        for ss, ee in intervals[1:]:
            if ss < last_ee:
                n_erase += 1
            else:
                last_ee = ee
        return n_erase