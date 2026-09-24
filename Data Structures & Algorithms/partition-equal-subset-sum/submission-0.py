class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total&1: return False
        target = total//2
        dp = set()
        dp.add(0)
        for n1 in nums:
            next_dp = set()
            next_dp.add(n1)
            for n2 in dp:
                nn = n1+n2
                if nn==target:
                    return True
                next_dp.add(nn)
                next_dp.add(n2)
            dp = next_dp
        return False