"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        if not intervals: return True
        pre_ee = intervals[0].end
        for x in intervals[1:]:
            if x.start< pre_ee:
                return False
            else:
                pre_ee = x.end
        return True