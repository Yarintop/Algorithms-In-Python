class NQueen:
    @staticmethod
    def nQueen(n, col=0, board=None, firstCall=True):
        """
            The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

        Args:
            n (int): The board's size
            col (int, optional): The current column. Defaults to 0.
            board (list (list (int)), optional): The current chess board. Defaults to None.
            firstCall (bool, optional): If we're in a recursive state or not. Defaults to True.

        Returns:
            Bool: If a configuration of the queens exists in a board with the size of N by N, print it and return True. Otherwise, return False.
        """
        if firstCall:
            board = [[0] * n for _ in range(n)]
            
        if col >= n:
            return True
        
        
        for row in range(n):
            if NQueen.isValid(n, board, col, row):
                board[row][col] = 1
                if NQueen.nQueen(n, col + 1, board, False):
                    if firstCall:
                        break
                    return True
                board[row][col] = 0
        else:
            board[row][col] = 0
            if firstCall:
                print("Solution could not be found.")
            return False
        
        for i in range(n):
            for j in range(n):
                print(board[i][j], end='\t')
            print()
        return True
    
    @staticmethod
    def isValid(n, board, col, row):
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        for i, j in zip(reversed(range(0, row)), reversed(range(0, col))):
            if board[i][j] == 1:
                return False
            
        for i, j in zip(range(row + 1, n), reversed(range(0, col))):
            if board[i][j] == 1:
                return False
        
        return True
            
if __name__ == "__main__":
    NQueen.nQueen(5)