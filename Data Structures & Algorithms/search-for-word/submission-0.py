class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(visited, rr, cc, idx, isExist):
            if self.n_word == idx:
                return True
            
            # up
            if rr-1>=0 and (rr-1,cc) not in visited and self.board[rr-1][cc]==self.word[idx] and not isExist:
                isExist = backtracking(visited+[(rr-1,cc)], rr-1, cc, idx+1, isExist)

            # down
            if rr+1<=self.Row-1 and (rr+1,cc) not in visited and self.board[rr+1][cc]==self.word[idx] and not isExist:
                isExist = backtracking(visited+[(rr+1,cc)], rr+1, cc, idx+1, isExist)

            # left
            if cc-1>=0 and (rr,cc-1) not in visited and self.board[rr][cc-1]==self.word[idx] and not isExist:
                isExist = backtracking(visited+[(rr,cc-1)], rr, cc-1, idx+1, isExist)

            # right
            if cc+1<=self.Col-1 and (rr,cc+1) not in visited and self.board[rr][cc+1]==self.word[idx] and not isExist:
                isExist = backtracking(visited+[(rr,cc+1)], rr, cc+1, idx+1, isExist)

            return isExist

        self.board = board
        self.word = word
        self.n_word = len(word)
        self.Row = len(board)
        self.Col = len(board[0])
        isExist = False
        for rr in range(self.Row):
            for cc in range(self.Col):
                if board[rr][cc] == word[0]:
                    isExist = backtracking([(rr,cc)], rr, cc, 1, isExist)
                    if isExist:
                        return isExist
        return isExist