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
        return result

def get_connect(state: State, n_player:int):
    if n_player == 0:
        cur_player_shape = GameConstant.PLAYER1_SHAPE
        cur_player_color = GameConstant.PLAYER1_COLOR
        cur_opponent_shape = GameConstant.PLAYER2_SHAPE
        cur_opponent_color = GameConstant.PLAYER2_COLOR
    else:
        cur_player_shape = GameConstant.PLAYER2_SHAPE
        cur_player_color = GameConstant.PLAYER2_COLOR
        cur_opponent_shape = GameConstant.PLAYER1_SHAPE
        cur_opponent_color = GameConstant.PLAYER1_COLOR

    # connect
    connect_list_cell = [[0 for x in range(3)] for direction in range(8)] # QWEDCXZA[3]

    toReturn = 0

    for row in range(state.board.row):
        for col in range(state.board.col):
            if (state.board[row,col].color == cur_player_color):
                for i in range(1,4):
                    # Q
                    if ((row+i) < state.board.row) and ((col-i) >= 0):
                        if (cur_opponent_shape == state.board[row+i,col-i].shape) or (cur_opponent_color == state.board[row+i,col-i].color):
                            if (cur_opponent_shape == state.board[row+i,col-i].shape) and (cur_opponent_color == state.board[row+i,col-i].color):
                                connect_list_cell[0] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row+i,col-i].shape) and (cur_opponent_color == state.board[row+i,col-i].color):
                                for x in connect_list_cell[0]:
                                    if (x == 1):
                                        connect_list_cell[0] = [0 for x in range(3)]
                        
                        if (i == 1) or (connect_list_cell[0][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row+i,col-i].shape):
                                connect_list_cell[0][i-1] = 2
                            elif state.board[row,col].color == state.board[row+i,col-i].color:
                                connect_list_cell[0][i-1] = 1

                    else:
                        connect_list_cell[0] = [0 for x in range(3)]
                    
                    # W
                    if (row+i) < state.board.row:
                        if (cur_opponent_shape == state.board[row+i,col].shape) or (cur_opponent_color == state.board[row+i,col].color):
                            if (cur_opponent_shape == state.board[row+i,col].shape) and (cur_opponent_color == state.board[row+i,col].color):
                                connect_list_cell[1] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row+i,col].shape) and (cur_opponent_color == state.board[row+i,col].color):
                                for x in connect_list_cell[1]:
                                    if (x == 1):
                                        connect_list_cell[1] = [0 for x in range(3)]
                        
                        if (i == 1) or (connect_list_cell[1][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row+i,col].shape):
                                connect_list_cell[1][i-1] = 2
                            elif state.board[row,col].color == state.board[row+i,col].color:
                                connect_list_cell[1][i-1] = 1


                    else:
                        connect_list_cell[1] = [0 for x in range(3)]

                    # E
                    if ((row+i) < state.board.row) and ((col+i) < state.board.col):
                        if (cur_opponent_shape == state.board[row+i,col+i].shape) or (cur_opponent_color == state.board[row+i,col+i].color):
                            if (cur_opponent_shape == state.board[row+i,col+i].shape) and (cur_opponent_color == state.board[row+i,col+i].color):
                                connect_list_cell[2] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row+i,col+i].shape) and (cur_opponent_color == state.board[row+i,col+i].color):
                                for x in connect_list_cell[2]:
                                    if (x == 1):
                                        connect_list_cell[2] = [0 for x in range(3)]
                        
                        if (i == 1) or (connect_list_cell[2][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row+i,col+i].shape):
                                connect_list_cell[2][i-1] = 2
                            elif state.board[row,col].color == state.board[row+i,col+i].color:
                                connect_list_cell[2][i-1] = 1

                    else:
                        connect_list_cell[2] = [0 for x in range(3)]

                    # D
                    if (col+i) < state.board.col:
                        if (cur_opponent_shape == state.board[row,col+i].shape) or (cur_opponent_color == state.board[row,col+i].color):
                            if (cur_opponent_shape == state.board[row,col+i].shape) and (cur_opponent_color == state.board[row,col+i].color):
                                connect_list_cell[3] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row,col+i].shape) and (cur_opponent_color == state.board[row,col+i].color):
                                for x in connect_list_cell[3]:
                                    if (x == 1):
                                        connect_list_cell[3] = [0 for x in range(3)]

                        if (i == 1) or (connect_list_cell[3][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row,col+i].shape):
                                connect_list_cell[3][i-1] = 2
                            elif state.board[row,col].color == state.board[row,col+i].color:
                                connect_list_cell[3][i-1] = 1

                    else:
                        connect_list_cell[3] = [0 for x in range(3)]

                    # C
                    if ((col+i) < state.board.col) and ((row-i) >= 0):
                        if (cur_opponent_shape == state.board[row-i,col+i].shape) or (cur_opponent_color == state.board[row-i,col+i].color):
                            if (cur_opponent_shape == state.board[row-i,col+i].shape) and (cur_opponent_color == state.board[row-i,col+i].color):
                                connect_list_cell[4] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row-i,col+i].shape) and (cur_opponent_color == state.board[row-i,col+i].color):
                                for x in connect_list_cell[4]:
                                    if (x == 1):
                                        connect_list_cell[4] = [0 for x in range(3)]

                        if (i == 1) or (connect_list_cell[4][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row-i,col+i].shape):
                                connect_list_cell[4][i-1] = 2
                            elif state.board[row,col].color == state.board[row-i,col+i].color:
                                connect_list_cell[4][i-1] = 1

                    else:
                        connect_list_cell[4] = [0 for x in range(3)]
                    
                    # X
                    if (row-i) >= 0:
                        if (cur_opponent_shape == state.board[row-i,col].shape) or (cur_opponent_color == state.board[row-i,col].color):
                            if (cur_opponent_shape == state.board[row-i,col].shape) and (cur_opponent_color == state.board[row-i,col].color):
                                connect_list_cell[5] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row-i,col].shape) and (cur_opponent_color == state.board[row-i,col].color):
                                for x in connect_list_cell[5]:
                                    if (x == 1):
                                        connect_list_cell[5] = [0 for x in range(3)]

                        if (i == 1) or (connect_list_cell[5][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row-i,col].shape):
                                connect_list_cell[5][i-1] = 2
                            elif state.board[row,col].color == state.board[row-i,col].color:
                                connect_list_cell[5][i-1] = 1

                    else:
                        connect_list_cell[5] = [0 for x in range(3)]

                    # Z
                    if ((row-i) >= 0) and ((col-i) >= 0):
                        if (cur_opponent_shape == state.board[row-i,col-i].shape) or (cur_opponent_color == state.board[row-i,col-i].color):
                            if (cur_opponent_shape == state.board[row-i,col-i].shape) and (cur_opponent_color == state.board[row-i,col-i].color):
                                connect_list_cell[6] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row-i,col-i].shape) and (cur_opponent_color == state.board[row-i,col-i].color):
                                for x in connect_list_cell[6]:
                                    if (x == 1):
                                        connect_list_cell[6] = [0 for x in range(3)]
                        
                        if (i == 1) or (connect_list_cell[6][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row-i,col-i].shape):
                                connect_list_cell[6][i-1] = 2
                            elif state.board[row,col].color == state.board[row-i,col-i].color:
                                connect_list_cell[6][i-1] = 1

                    else:
                        connect_list_cell[6] = [0 for x in range(3)]
                    
                    # A
                    if (col-i) >= 0:
                        if (cur_opponent_shape == state.board[row,col-i].shape) or (cur_opponent_color == state.board[row,col-i].color):
                            if (cur_opponent_shape == state.board[row,col-i].shape) and (cur_opponent_color == state.board[row,col-i].color):
                                connect_list_cell[7] = [0 for x in range(3)]
                            elif (cur_opponent_shape != state.board[row,col-i].shape) and (cur_opponent_color == state.board[row,col-i].color):
                                for x in connect_list_cell[7]:
                                    if (x == 1):
                                        connect_list_cell[7] = [0 for x in range(3)]
                        
                        if (i == 1) or (connect_list_cell[7][i-2] != 0):
                            if (cur_player_shape == state.board[row,col].shape) and (state.board[row,col].shape == state.board[row,col-i].shape):
                                connect_list_cell[7][i-1] = 2
                            elif state.board[row,col].color == state.board[row,col-i].color:
                                connect_list_cell[7][i-1] = 1

                    else:
                        connect_list_cell[7] = [0 for x in range(3)]
                
                for x in connect_list_cell:
                    connect_4_shape = True
                    connect_4_color = True
                    for y in x:
                        toReturn += y
                        if y != 2:
                            connect_4_shape = False
                        if y == 0:
                            connect_4_color = False

                    if connect_4_shape:
                        return 99
                    elif connect_4_color:
                        return 49

                connect_list_cell = [[0 for x in range(3)] for direction in range(8)]

    return toReturn

def objective_function(state: State, n_player: int):
    if (n_player == 0):
        print("obj player 1",heuristic_function(state, n_player) , get_connect(state, n_player) ,get_connect(state, 1))
        return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 1)
    else:
        print("obj player 2", heuristic_function(state, n_player) , get_connect(state, n_player) , get_connect(state, 0))
        return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 0)