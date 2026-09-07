class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        paths = {}
        for src, dest, tt in times:
            if src not in paths:
                paths[src] = [(dest, tt)]
            else:
                paths[src] += [(dest, tt)]

        if k not in paths:
            return -1

        q = [(k,0)]     # (src, time)
        arrived = [float('inf')]*(n+1)
        arrived[0] = 0
        arrived[k] = 0
        while q:
            src, tt = q.pop(0)
            if src in paths:
                for dest, dt in paths[src]:
                    if arrived[dest]>tt+dt:
                        arrived[dest]=tt+dt
                        q.append((dest, tt+dt))
        ans = max(arrived)
        if ans != float("inf"):
            return ans
        return -1