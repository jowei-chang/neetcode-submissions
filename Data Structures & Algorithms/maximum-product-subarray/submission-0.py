class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxmax = 1
        minmin = 1
        res = nums[0]
        for nn in nums:
            tmp = max(maxmax*nn, minmin*nn, nn)
            minmin = min(maxmax*nn, minmin*nn, nn)
            maxmax = tmp
            res = max(res, maxmax)
        return res