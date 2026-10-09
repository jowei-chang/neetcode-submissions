class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = False, False, False
        at, bt, ct = target
        for ai, bi, ci in triplets:
            if ai<=at and bi<=bt and ci<=ct:
                if ai==at:a=True
                if bi==bt:b=True
                if ci==ct:c=True
        if a and b and c: return True
        return False