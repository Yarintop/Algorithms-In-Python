class TheKnightsTour:
    @staticmethod
    def theKnightsTour(n, move=0, currX=0, currY=0, board=None):
        """
            The Knight's Tour Algorithm assumes we have an NxN chess board and the knights starts on the 0, 0 position.
            Is there a configuration where the knight jumps to every single cell only once? and if there is, return it.

        Args:
            n (int): Chess board is N by N
            move (int, optional): The current move. Defaults to 0.
            currX (int, optional): The current x. Defaults to 0.
            currY (int, optional): The current y. Defaults to 0.
            board ([type], optional): The current chess Board. Defaults to None.

        Returns:
            [type]: [description]
        """
        if move == 0:
            board = [[-1] * n for _ in range(n)]
            
        if currX < 0 or currX >= n or currY < 0 or currY >= n or board[currX][currY] != -1:
            return None
        
        board[currX][currY] = move
        if move == (n ** 2) - 1:
            return True

        movesX= [2, 1, -1, -2, -2, -1, 1, 2]
        movesY = [1, 2, 2, 1, -1, -2, -2, -1]
        
        for offsetX, offsetY in zip(movesX, movesY):
            if TheKnightsTour.theKnightsTour(n, move + 1, currX + offsetX, currY + offsetY, board):
                if move == 0:
                    break
                return True
        else:
            board[currX][currY] = -1
            if move == 0:
                print("Solution could not be found.")
            return False
        
        for i in range(n):
            for j in range(n):
                print(board[i][j], end='\t')
            print()
            
if __name__ == "__main__":
    TheKnightsTour.theKnightsTour(8)