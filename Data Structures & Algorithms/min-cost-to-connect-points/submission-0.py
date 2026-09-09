class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        visited = set()
        cost = 0
        min_heap = [(0,0)]      # (distance, index)

        while len(visited) < N:
            d, ii = heapq.heappop(min_heap)
            if ii in visited:
                continue
            visited.add(ii)
            cost += d
            xi, yi = points[ii]

            for jj in range(N):
                if jj not in visited:
                    xj, yj = points[jj]
                    dd = abs(xj-xi)+abs(yj-yi)
                    heapq.heappush(min_heap,(dd, jj))
        return cost