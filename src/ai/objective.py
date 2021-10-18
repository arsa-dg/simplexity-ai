from src.constant import GameConstant
from src.model import State

def heuristic_function(state: State, n_player: int):
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
                    elif(piece.color == GameConstant.PLAYER2_COLOR):
                        result -= scores[row][col]
        else:
            for row in range(state.board.row):
                for col in range(state.board.col):
                    piece = state.board[row, col]
                    if(piece.color == GameConstant.PLAYER2_COLOR):
                        result += scores[row][col]
                    elif(piece.color == GameConstant.PLAYER1_COLOR):
                        result -= scores[row][col]
        print("result heu", result)
        return result

def get_connect(state: State, n_player:int):
    print("player" , n_player)
    if n_player == 0:
        cur_player_shape = GameConstant.PLAYER1_SHAPE
        cur_player_color = GameConstant.PLAYER1_COLOR
    else:
        cur_player_shape = GameConstant.PLAYER2_SHAPE
        cur_player_color = GameConstant.PLAYER2_COLOR

    # connect
    connect_list = []
    for row in range(state.board.row):
        for col in range(state.board.col):
            if (state.board[row,col].color == cur_player_color) or (state.board[row,col].shape == cur_player_shape):
                for i in range(3):
                    # Q
                    if (row+i) < state.board.row and (col-i) >= 0:
                        if (cur_player_color == state.board[row+i,col-i].color) or (cur_player_shape == state.board[row+i,col-i].shape):
                            temp = [[row,col],[row+i,col-i]]
                            connect_list.append(temp)
                    
                    # W
                    if (row+i) < state.board.row:
                        if (cur_player_color == state.board[row+i,col].color) or (cur_player_shape == state.board[row+i,col].shape):
                            temp = [[row,col],[row+i,col]]
                            connect_list.append(temp)

                    # E
                    if (row+i) < state.board.row and (col+i) < state.board.col:
                        if (cur_player_color == state.board[row+i,col+i].color) or (cur_player_shape == state.board[row+i,col+i].shape):
                            temp = [[row,col],[row+i,col+i]]
                            connect_list.append(temp)

                    # D
                    if (col+i) < state.board.col:
                        if (cur_player_color == state.board[row,col+i].color) or (cur_player_shape == state.board[row,col+i].shape):
                            temp = [[row,col],[row,col+i]]
                            connect_list.append(temp)

                    # C
                    if (col+i) < state.board.col and (row-i) >= 0:
                        if (cur_player_color == state.board[row-i,col+i].color) or (cur_player_shape == state.board[row-i,col+i].shape):
                            temp = [[row,col],[row-i,col+i]]
                            connect_list.append(temp)
                    
                    # X
                    if (row-i) >= 0:
                        if (cur_player_color == state.board[row-i,col].color) or (cur_player_shape == state.board[row-i,col].shape):
                            temp = [[row,col],[row-i,col]]
                            connect_list.append(temp)

                    # Z
                    if (row-i) >= 0 and (col-i) >= 0:
                        if (cur_player_color == state.board[row-i,col-i].color) or (cur_player_shape == state.board[row-i,col-i].shape):
                            temp = [[row,col],[row-i,col-i]]
                            connect_list.append(temp)
                    
                    # A
                    if (col-i) >= 0:
                        if (cur_player_color == state.board[row,col-i].color) or (cur_player_shape == state.board[row,col-i].shape):
                            temp = [[row,col],[row,col-i]]
                            connect_list.append(temp)

    return len(connect_list)

def objective_function(state: State, n_player: int):
    if (n_player == 0):
        print("obj player 1",heuristic_function(state, n_player) , get_connect(state, n_player) ,get_connect(state, 1))
        return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 1)
    else:
        print("obj player 2", heuristic_function(state, n_player) , get_connect(state, n_player) , get_connect(state, 0))
        return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 0)