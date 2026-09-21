import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        n_dp = 1
        for nn in nums[1:]:
            pos = bisect.bisect_left(dp, nn)
            if pos == n_dp:
                dp.append(nn)
                n_dp+=1
            else:
                dp[pos] = nn
        return n_dp