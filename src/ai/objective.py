from src.constant import GameConstant
from src.model import State

def objective_function(state: State, n_player: int): #sek ngawur
        # if n_player % 2 == 0: #player1
            #dibandingkan sebelahnya dengan shape,col player 1
        # else: #player2
        scores = [
            [3, 4, 5, 7, 5, 4, 3],
            [4, 6, 8, 10, 8, 6, 4],
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [3, 4, 5, 7, 5, 4, 3],
        ]

        result = 0
        
        if(n_player==0): # player 1
            for row in range(state.board.row):
                for col in range(state.board.col):
                    piece = state.board[row, col]
                    if(piece.color == GameConstant.PLAYER1_COLOR):
                        result += scores[row][col]
                    else:
                        result -= scores[row][col]
        else:
            for row in range(state.board.row):
                for col in range(state.board.col):
                    piece = state.board[row, col]
                    if(piece.color == GameConstant.PLAYER2_COLOR):
                        result += scores[row][col]
                    else:
                        result -= scores[row][col]
        return result