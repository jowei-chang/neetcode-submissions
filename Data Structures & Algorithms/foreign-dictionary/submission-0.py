class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = collections.defaultdict(set)
        pre_order = {ww:0 for word in words for ww in word}

        for word1, word2 in zip(words, words[1:]):
            for w1, w2 in zip(word1, word2):
                if w1!=w2:
                    if w2 not in adj[w1]:
                        adj[w1].add(w2)
                        pre_order[w2] +=1
                    break
            else:
                if len(word1)>len(word2):
                    return ""
        que = collections.deque([ww for ww in pre_order if pre_order[ww]==0])
        res = []
        while que:
            cur = que.popleft()
            res.append(cur)
            for next in adj[cur]:
                pre_order[next] -= 1
                if pre_order[next]==0:
                    que.append(next)
        if len(pre_order)>len(res):     # has cycle
            return ""
        return "".join(res)