class Solution:
    def jump(self, nums: List[int]) -> int:
        maxStep = nums[0]
        idx=0
        N = len(nums)
        n_jump = 0
        if N<=1:return n_jump
        while idx<N:
            n_jump+=1
            if maxStep>=N-1:
                return n_jump
            tmpStep = 0
            for ii in range(idx, maxStep+1):
                tmpStep = max(tmpStep, ii+nums[ii])
            idx=maxStep+1
            maxStep = tmpStep
            
        return n_jump