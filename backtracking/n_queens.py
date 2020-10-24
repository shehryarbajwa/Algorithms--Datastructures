class Solution:
    def solveNQueens(self, n):
        self.n = n
        result = []
        board = [["." for _ in range(self.n)] for _ in range(self.n)]
        self.placeQueens(board, 0, result)
        return result
    
    def placeQueens(self, board, row, result):
        if row >= self.n:
            newResult = [''.join(x) for x in board]
            result.append(newResult)
        
        for col in range(self.n):
            if self.isSafe(board, row, col):
                board[row][col] = "Q"
                self.placeQueens(board, row + 1, result)
                #backtracking step
                board[row][col] = "."
    
    def isSafe(self, board, row, col):
        # check this whole col up down
        for r in range(row):
            if board[r][col] == "Q":
                return False
        
        # check upper left diagonal
        for r, c in zip(range(row, -1, -1),
                    range(col, -1, -1)):
            if board[r][c] == "Q":
                return False

        # check upper right diagonal
        for r, c in zip(range(row, -1, -1),
                    range(col, self.n)):
            if board[r][c] == "Q":
                return False
        return True

n = Solution()
print(n.solveNQueens(3))