class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        chk = set()

        for ii in range(len(nums)):
            if nums[ii] in chk:
                return nums[ii]
            else:
                chk.add(nums[ii])