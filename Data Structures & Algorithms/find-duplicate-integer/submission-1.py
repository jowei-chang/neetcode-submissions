class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        chk = set()
        for ii in range(len(nums)):
            
            if nums[ii] not in chk:
                chk.add(nums[ii])
            else:
                return nums[ii]
                