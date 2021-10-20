from os import startfile, stat
import random
from time import struct_time
from src.model.piece import Piece
from time import time

from src.constant import ShapeConstant, GameConstant, ColorConstant
from src.model import State
import copy
from typing import Tuple

from src.ai.objective import objective_function, get_connect
from src.utility import is_win, is_full, place

class Minimax:
    def __init__(self):
        self.min = 99999
        self.max = -99999

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:

        alpha = self.max  
        beta = self.min
        
        start = time()
        _, best_move = self.minimax(state, n_player, thinking_time, alpha, beta, start, 0)
        print(best_move)
        return best_move                                                                               
        
    def minimax(self, state: State, n_player: int, thinking_time: float, alpha: int, beta: int, start: float, depth:int):

        self.thinking_time = time() + thinking_time

        if is_win(state.board)!=None or is_full(state.board) or time()-start>thinking_time-0.1 or depth==6:
            return [get_connect(state, n_player), None]
            
        if(n_player==0):
            best = self.max
            best_move = (None,None)

            for col in range(state.board.col):
                for shape in [ShapeConstant.CIRCLE, ShapeConstant.CROSS]:
                    possible_state = copy.deepcopy(state)

                    placement = place(possible_state, n_player, shape, col)
                    if(placement!=-1):
                        score, _  = self.minimax(possible_state, 1, thinking_time, alpha, beta, start, depth+1)
                        
                        if(score>best):
                            best_move = (col, shape)

                        best = max(best, score)
                        alpha = max(alpha, best)

                        if beta<=alpha:
                            break
                if beta<=alpha:
                    break
                        
            # print('maks player')
            # print("time", time()-start)
            # print("best move", best_move)
            # print("best score", best)
            # print()
            return [best, best_move]
        else:
            best = self.min
            best_move = (None,None)

            for col in range(state.board.col):
                for shape in [ShapeConstant.CROSS, ShapeConstant.CIRCLE]:
                        possible_state = copy.deepcopy(state)
 
                        placement = place(possible_state, n_player, shape, col)
                        if(placement!=-1):
                            score, _  = self.minimax(possible_state, 0, thinking_time, alpha, beta, start, depth+1)

                            if(score<best):
                                best_move = (col, shape)
                            best = min(best, score)
                            beta = min(beta, best)

                            if beta<=alpha:
                                break
                if beta<=alpha:
                    break

            # print('mini player')
            # print("time", time()-start)
            # print("best move", best_move)
            # print("best score", best)
            # print()
            return [best, best_move]

