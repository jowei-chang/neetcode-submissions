class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N==1: return nums[0]
        if N==2: return max(nums)
        rob0_pre2, rob0_pre1 = nums[0], nums[0]
        rob1_pre2, rob1_pre1 = 0, nums[1]
        for ii in range(2, N):
            if ii==N-1:
                cur0 = max(rob0_pre1, rob0_pre2)
                cur1 = max(rob1_pre1, rob1_pre2+nums[ii])
                return max(cur0, cur1)
            else:
                cur0 = max(rob0_pre1, rob0_pre2+nums[ii])
                rob0_pre2 = rob0_pre1
                rob0_pre1 = cur0
                cur1 = max(rob1_pre1, rob1_pre2+nums[ii])
                rob1_pre2 = rob1_pre1
                rob1_pre1 = cur1