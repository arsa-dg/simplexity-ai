import random
import copy
from time import time

from src.constant import ShapeConstant
from src.model import State
from src.utility import place

from typing import Tuple, List


class LocalSearch:
    def __init__(self):
        self.current_values = [-99999, 999999]

    def objective_function(self, state: State, n_player: int): #sek ngawur
        # if n_player % 2 == 0: #player1
            #dibandingkan sebelahnya dengan shape,col player 1
        # else: #player2

        return 1

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        print("find")
        self.thinking_time = time() + thinking_time
        self.temp_state = state
        # itung nilai state skrg
        # harusnya disimpen semua yg dibutuhin di rumus obj function biar cepet
        if (self.current_values[n_player] is None):
            current_state_value = self.objective_function(state, n_player)
        else:
            current_state_value = self.current_values[n_player]

        best_state = state
        best_state_value = current_state_value
        best_col = -1
        best_shape = ShapeConstant.CROSS
        
        # iterasi semua kemungkinan
        for col in range(state.board.col):
            for shape in [ShapeConstant.CROSS, ShapeConstant.CIRCLE]: #sek ngawur
                # ambil state lama buat dicoba2
                possible_state = copy.deepcopy(state)
                print("col = ", col)
                print("shape = ", shape)
                possible_placement = place(possible_state, n_player, shape, col)

                # peletakan ga valid, coba kemungkinan lain
                if possible_placement == -1:
                    continue

                print("possible board\n")
                print(possible_state.board)

                # cari nilai dari kemungkinan state
                possible_state_value = self.objective_function(possible_state, n_player)
                # compare nilai kemungkinan state sama nilai state yg skrg
                # kalo ada yg sama gapapa
                # TODO: tentuin yg sama mau diambil lgsg aja atau mau dikumpulin trus dirandom
                if (best_state_value <= possible_state_value):
                    best_state = possible_state
                    best_state_value = possible_state_value
                    best_col = col
                    best_shape = shape
    
        # simpan value buat referensi turn selanjutnya
        self.current_values[n_player] = best_state_value

        best_movement = (best_col, best_shape) 

        return best_movement