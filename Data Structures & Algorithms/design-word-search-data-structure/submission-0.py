class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ww in word:
            if ww not in node:
                node[ww] = {}
            node = node[ww]
        node["end"] = True

    def search(self, word: str) -> bool:
        def dfs(node, idx, word, n):
            if idx==n:
                return "end" in node
            
            if word[idx]==".":
                for ww in node:
                    if ww != "end" and dfs(node[ww], idx+1, word, n):
                        return True
            elif word[idx] in node:
                return dfs(node[word[idx]], idx+1, word, n)
            return False

        return dfs(self.root, 0, word, len(word))
