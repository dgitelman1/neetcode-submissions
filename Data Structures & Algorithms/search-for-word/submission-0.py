class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for each letter, if it starts with the first word, we can check to see if we can make the word from that starting point
        # our function should return true if possible to make the word
        # at each point we should go on and see if we can make the subpart of that word from that point
        in_word = [[False]*len(board[0]) for _ in range(len(board))]
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def backtrack(i, j, cur_word):
            if len(cur_word)==0:
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return False
            if in_word[i][j] or board[i][j]!=cur_word[0]:
                return False
            in_word[i][j]=True
            for up, down in directions:
                if backtrack(i+up, j+down, cur_word[1:]):
                    return True
            in_word[i][j]=False
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, word):
                    return True
        return False