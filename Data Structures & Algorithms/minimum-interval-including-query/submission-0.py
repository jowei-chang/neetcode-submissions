class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []       # (length or intervals, right side)
        res = {}
        idx = 0
        N = len(intervals)
        for qq in sorted(queries):
            # put any intervals including qq into a minHeap
            while idx < N and intervals[idx][0]<=qq:
                l, r = intervals[idx]
                heapq.heappush(heap, (r-l+1, r))
                idx+=1

            # remove all intervals from the minHeap that do not contain qq.
            while heap and heap[0][1]<qq:
                heapq.heappop(heap)
            res[qq] = heap[0][0] if heap else -1
        return [res[qq] for qq in queries]