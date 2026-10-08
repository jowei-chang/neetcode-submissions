class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N%groupSize!=0: return False
        hand.sort()
        table = collections.defaultdict(int)
        for nn in hand:
            table[nn]+=1

        for ii in range(N):
            if table[hand[ii]]>0:
                for jj in range(hand[ii], hand[ii]+groupSize):
                    if table[jj]>0:
                        table[jj]-=1
                    else:
                        return False
        return True