class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for nn in nums:
            x ^= nn     # bit operation: XOR
        return x