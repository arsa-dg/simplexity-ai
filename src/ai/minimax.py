from os import startfile, stat
import random
from time import time
from src.model.piece import Piece

from src.constant import ShapeConstant, GameConstant, ColorConstant
# from src.utility import place
from src.model import State
import copy
from typing import Tuple, List, no_type_check, Dict

from src.ai.objective import objective_function
from src.utility import is_win, is_full, place

class Minimax:
    def __init__(self):
        self.min = 99999
        self.max = -99999

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        move = (-2, ShapeConstant.BLANK)
        # blank = Piece(ShapeConstant.BLANK, ColorConstant.BLACK)
        
        possible_state = copy.deepcopy(state)

        start = time()
        mikir = start + thinking_time
        if(n_player==0):
            best = self.max
            for col in range(possible_state.board.col):
                for shape in [ShapeConstant.CROSS, ShapeConstant.CIRCLE]:
                        placement = -1
                        if possible_state.players[n_player].quota[shape] == 0:
                            continue

                        for row in range(possible_state.board.row - 1, -1, -1):
                            if possible_state.board[row, col].shape == ShapeConstant.BLANK:
                                piece = Piece(shape, GameConstant.PLAYER_COLOR[n_player])
                                possible_state.board.set_piece(row, col, piece)
                                possible_state.players[n_player].quota[shape] -= 1
                                placement = row
                                break

                        if(placement==-1):
                            continue

                        print("player max")
                        print("placement", placement, col, shape)
                        score, times = self.minimax(possible_state, 1, thinking_time, self.max, self.min, start)

                        if(score>best):
                            best = score
                            move = (col, shape)

                        print("waktu", times)
                        if(times>mikir-0.15):
                            # print("waktu", times)

                            return move
            return move
        else:
            best = self.min
            for col in range(possible_state.board.col):
                for shape in [ShapeConstant.CROSS, ShapeConstant.CIRCLE]:
                        placement = -1
                        if possible_state.players[n_player].quota[shape] == 0:
                            continue

                        for row in range(possible_state.board.row - 1, -1, -1):
                            if possible_state.board[row, col].shape == ShapeConstant.BLANK:
                                piece = Piece(shape, GameConstant.PLAYER_COLOR[n_player])
                                possible_state.board.set_piece(row, col, piece)
                                possible_state.players[n_player].quota[shape] -= 1
                                placement = row
                                break

                        if(placement==-1):
                            continue

                        print("placement", placement, col, shape)
                        score, times = self.minimax(possible_state, 0, thinking_time, self.max, self.min, start)

                        if(score<best):
                            best = score
                            move = (col, shape)

                        print("waktu", times)
                        if(times>mikir-0.15):
                            return move

            return move 

    def minimax(self, state: State, n_player: int, thinking_time: float, alpha: int, beta: int, start: float) -> List[Dict[int, float]]:

        self.thinking_time = time() + thinking_time

        winner = is_win(state.board)
        if winner!=None or is_full(state.board) or time()-start>thinking_time-0.5:
            return [objective_function(state, n_player), time()-start]

        # blank = Piece(ShapeConstant.BLANK, ColorConstant.BLACK)

        # possible_state = copy.deepcopy(state)
        
        if(n_player==0):
            # print("player max")
            
            best = self.max

            for col in range(state.board.col):
                for shape in [ShapeConstant.CROSS, ShapeConstant.CIRCLE]:
                        placement = -1
                        if state.players[n_player].quota[shape] == 0:
                            continue
                        
                        for row in range(state.board.row - 1, -1, -1):
                            if state.board[row, col].shape == ShapeConstant.BLANK:
                                piece = Piece(shape, GameConstant.PLAYER_COLOR[n_player])
                                state.board.set_piece(row, col, piece)
                                state.players[n_player].quota[shape] -= 1
                                placement = row
                                break

                        if(placement==-1):
                            continue

                        score, _ = self.minimax(state, 1, thinking_time, alpha, beta, start)

                        best = max(best, score)
                        alpha = max(alpha, best)
                        
                        if beta<=alpha:
                            break
                if beta<=alpha:
                            break
                       
            return [best, time()-start]
        else:
            # print("player min")

            best = self.min

            for col in range(state.board.col):
                for shape in [ShapeConstant.CROSS, ShapeConstant.CIRCLE]:
                        placement = -1
                        if state.players[n_player].quota[shape] == 0:
                            continue

                        for row in range(state.board.row - 1, -1, -1):
                            if state.board[row, col].shape == ShapeConstant.BLANK:
                                piece = Piece(shape, GameConstant.PLAYER_COLOR[n_player])
                                state.board.set_piece(row, col, piece)
                                state.players[n_player].quota[shape] -= 1
                                placement = row
                                break

                        if(placement==-1):
                            continue

                        score, _ = self.minimax(state, 0, thinking_time, alpha, beta, start)
                
                        best = min(best, score)
                        beta = min(beta, best)
                    
                        if beta<=alpha:
                            break
                if beta<=alpha:
                            break

            return [best, time()-start]

