"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0: return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        h = [intervals[0].end]
        for x in intervals[1:]:
            if h and h[0]<=x.start:
                heapq.heappop(h)
            heapq.heappush(h, x.end)
        return len(h)