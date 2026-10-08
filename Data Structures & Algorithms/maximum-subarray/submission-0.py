class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = 0
        maxmax = -float("inf")
        minmin = 0
        for nn in nums:
            acc += nn
            maxmax = max(maxmax, acc-minmin)
            minmin = min(minmin, acc)
        return maxmax