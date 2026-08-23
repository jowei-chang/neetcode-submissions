class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ww in word:
            if ww not in node:
                node[ww] = {}
            node = node[ww]
        node["end"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for ww in word:
            if ww not in node:
                return False
            node = node[ww]
        return "end" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ww in prefix:
            if ww not in node:
                return False
            node = node[ww]
        return True
        