class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost) < 0: return -1
        idx = 0
        res = 0
        for ii in range(len(gas)):
            res += gas[ii]-cost[ii]
            if res < 0:
                res = 0
                idx = ii+1
        return idx