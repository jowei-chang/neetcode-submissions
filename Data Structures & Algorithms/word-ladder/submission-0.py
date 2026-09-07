class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        lw = len(wordList[0])
        visited = set(beginWord)
        adj = {}
        for ww in wordList:
            for ii in range(lw):
                pattern = ww[:ii]+"*"+ww[ii+1:]
                if pattern not in adj:
                    adj[pattern] = [ww]
                else:
                    adj[pattern] += [ww]
        q = [(beginWord, 1)]
        while q:
            word, step = q.pop(0)
            if word==endWord:
                return step
            for ii in range(lw):
                pattern = word[:ii]+"*"+word[ii+1:]
                for ww in adj[pattern]:
                    if ww in visited:
                        continue
                    visited.add(ww)
                    q.append((ww,step+1))
        return 0