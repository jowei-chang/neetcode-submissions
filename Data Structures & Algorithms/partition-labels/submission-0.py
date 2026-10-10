class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        table = collections.defaultdict(int)
        for ii, ss in enumerate(s):
            table[ss]=ii

        idx=0
        ans = []
        while idx<len(s):
            l = idx
            buf = set()
            buf.add(s[idx])
            r = table[s[idx]]
            while idx < r:
                idx+=1
                if s[idx] not in buf:
                    buf.add(s[idx])
                    r = max(r, table[s[idx]])
            ans.append(r-l+1)
            idx+=1
        return ans