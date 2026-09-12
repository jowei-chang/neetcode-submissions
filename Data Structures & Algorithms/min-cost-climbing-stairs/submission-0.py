class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step2 = cost[0]
        step1 = cost[1]
        cost.append(0)
        for ii in range(2,len(cost)):
            cur = min(step1, step2)+cost[ii]
            step2 = step1
            step1 = cur
        return cur