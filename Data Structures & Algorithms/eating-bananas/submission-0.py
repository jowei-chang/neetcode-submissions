class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)+1
        ans = r -1
        while l < r:
            mid = (l+r)//2
            if mid < 1: return 1

            acc = 0
            for nn in piles:
                acc += nn//mid
                if nn%mid != 0:
                    acc += 1

            if acc <= h:
                r = mid
                ans = mid
            else:
                l = mid+1
        return ans