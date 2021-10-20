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

def get_connect(state: State, n_player: int):
    def check_direction(cur_shape, cur_color, cur_opponent_color, row, col):
        if state.board[row,col].color == cur_color:
            if state.board[row,col].shape == cur_shape:
                return 2
            return 1
        
        elif state.board[row,col].color == cur_opponent_color:
            if state.board[row,col].shape == cur_shape:
                return -1
            return -2
        
        return 0 
    
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

    to_return = 0

    connect_cell = [[0 for plus in range(3)] for direction in range(8)] # QWEDCXZA[3]

    for row in range(state.board.row):
        for col in range(state.board.col):
            if state.board[row,col].color == cur_player_color:
                for plus in range(1,4):
                    # Cek cell + plus
                    # Q
                    if ((row+plus) < state.board.row) and ((col-plus) >= 0):
                        connect_cell[0][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row+plus, col-plus)
                    else:
                        connect_cell[0] = [0 for plus in range(3)]
                    # W
                    if (row+plus) < state.board.row:
                        connect_cell[1][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row+plus, col)
                    else:
                        connect_cell[1] = [0 for plus in range(3)]
                    # E
                    if ((row+plus) < state.board.row) and ((col+plus) <state.board.col):
                        connect_cell[2][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row+plus, col+plus)
                    else:
                        connect_cell[2] = [0 for plus in range(3)]
                    # D
                    if (col+plus) < state.board.col:
                        connect_cell[3][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row, col+plus)
                    else:
                        connect_cell[3] = [0 for plus in range(3)]
                    # C
                    if ((row-plus) >= 0) and ((col+plus) < state.board.col):
                        connect_cell[4][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row-plus, col+plus)
                    else:
                        connect_cell[4] = [0 for plus in range(3)]
                    # X
                    if (row-plus) >= 0:
                        connect_cell[5][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row-plus, col)
                    else:
                        connect_cell[5] = [0 for plus in range(3)]
                    # Z
                    if ((row-plus) >= 0) and ((col-plus) >= 0):
                        connect_cell[6][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row-plus, col-plus)
                    else:
                        connect_cell[6] = [0 for plus in range(3)]
                    # A
                    if (col-plus) >= 0:
                        connect_cell[7][plus-1] = check_direction(cur_player_shape, cur_player_color, cur_opponent_color, row, col-plus)
                    else:
                        connect_cell[7] = [0 for plus in range(3)]
                
                # print(row,col,connect_cell) # bentaran
                # Hitung connect
                for direction in range(8):
                    temp = 0
                    is_connect_4_shape = True
                    is_connect_4_color = True
                    is_blocking = True

                    for plus in range(3):
                        if connect_cell[direction][plus] >= 0:
                            is_blocking = False

                            if (plus == 0) or (temp != 0):
                                if connect_cell[direction][plus] == 1:
                                    is_connect_4_shape = False
                                    temp += connect_cell[direction][plus]

                                elif connect_cell[direction][plus] == 2:
                                    if temp == (2*plus):
                                        temp += connect_cell[direction][plus]
                                    else:
                                        temp += 1
                                
                                else:
                                    is_connect_4_shape = False
                                    is_connect_4_color = False
                        
                        else:
                            is_connect_4_color = False

                            if connect_cell[direction][plus] == -2:
                                is_connect_4_shape = False
                                temp = 0
                            else:
                                if temp == (2*plus):
                                    temp += 2
                                else:
                                    temp = 0
                    
                    to_return += temp
                    if is_connect_4_shape:
                        to_return += 99
                    if is_connect_4_color:
                        to_return += 79
                    if is_blocking:
                        to_return += 49

                # reset connect_cell
                connect_cell = [[0 for plus in range(3)] for direction in range(8)]

    return to_return

def objective_function(state: State, n_player: int, chosen_shape: str = "-"):
    if (n_player == 0):
        # print(heuristic_function(state, n_player), get_connect(state, n_player), get_connect(state, 1))
        if(chosen_shape == GameConstant.PLAYER1_SHAPE):
            return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 1) + 2
        elif(chosen_shape == GameConstant.PLAYER2_SHAPE):
            return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 1) + 1
        else:
            return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 1)
    else:
        # print(heuristic_function(state, n_player), get_connect(state, n_player), get_connect(state, 0))
        if(chosen_shape == GameConstant.PLAYER2_SHAPE):
            return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 0) + 2
        elif(chosen_shape == GameConstant.PLAYER1_SHAPE):
            return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 0) + 1
        else:
            return heuristic_function(state, n_player) + get_connect(state, n_player) - get_connect(state, 0)