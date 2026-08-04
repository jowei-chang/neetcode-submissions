class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0]*26
        total = len(tasks)
        for tt in tasks:
            counts[ord(tt)-65] += 1
        maxmax = max(counts)
        max_times = counts.count(maxmax)
        ans = (maxmax-1)*n+maxmax+max_times-1
        if ans < total:
            return total
        return ans