class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(parent, rr, cc):
            if rr<0 or rr==self.R or cc<0 or cc==self.C or self.board[rr][cc] not in parent:
                return
            ch = self.board[rr][cc]
            
            self.board[rr][cc] = "*"
            node = parent[ch]
            # print("node: ", node)
            word = node.pop("end", None)
            if word: self.ans.append(word)

            dfs(node, rr-1, cc)
            dfs(node, rr+1, cc)
            dfs(node, rr, cc-1)
            dfs(node, rr, cc+1)

            self.board[rr][cc] = ch

            # Delete the found words
            if not node:
                # print("node: ", node)
                parent.pop(ch)

        self.trie = {}
        self.ans = []
        self.R, self.C = len(board), len(board[0])
        self.board = board

        # trie add word
        for word in words:
            node = self.trie
            for ww in word:
                if ww not in node:
                    node[ww] = {}
                node = node[ww]
            node["end"] = word

        for rr in range(self.R):
            for cc in range(self.C):
                dfs(self.trie, rr, cc)
        return self.ans