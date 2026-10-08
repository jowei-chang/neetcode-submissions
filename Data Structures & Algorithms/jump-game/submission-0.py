class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        maxStep = 0
        for ii, nn in enumerate(nums):
            if ii<=maxStep and nums[ii]+ii>maxStep:
                maxStep = nums[ii]+ii
        if maxStep>=N-1:
            return True
        return False