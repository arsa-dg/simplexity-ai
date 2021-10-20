import random
import copy
from time import time

from src.ai.objective import objective_function

from src.constant import ShapeConstant
from src.model import State
from src.utility import place

from typing import Tuple


class LocalSearch:
    def __init__(self):
        pass

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        self.thinking_time = time() + thinking_time
        current_state_value = objective_function(state, n_player, "-")

        best_state_value = current_state_value
        best_col = None
        best_shape = None

        equal_state_value = current_state_value
        equal_best_placements = []
        
        # iterasi semua kemungkinan
        for col in range(state.board.col):
            remaining_time = self.thinking_time - time()
            
            if remaining_time < 0.00005:
                break
        
            for shape in [ShapeConstant.CROSS, ShapeConstant.CIRCLE]: #sek ngawur
                # ambil state lama buat dicoba2
                if remaining_time < 0.00005:
                    break

                possible_state = copy.deepcopy(state)
                shape_quota = possible_state.players[n_player].quota

                if shape_quota.get(shape) == 0:
                    continue

                possible_placement = place(possible_state, n_player, shape, col)

                # peletakan ga valid, coba kemungkinan lain
                if possible_placement == -1:
                    continue

                # kalo mau ngecek ilangin komen printnya
                # print(possible_state.board)

                # cari nilai dari kemungkinan state
                # print('current value', current_state_value)
                possible_state_value = objective_function(possible_state, n_player, shape)
                # print(possible_state_value)
                if (best_state_value < possible_state_value):
                    best_state_value = possible_state_value
                    best_col = col
                    best_shape = shape
                    equal_best_placements = []
                    equal_best_placements.append([best_col, best_shape])
                elif (best_state_value == possible_state_value):
                    equal_best_placements.append([col, shape])

        if len(equal_best_placements) > 1:
            print('RANDOM GARA2 ADA YG SAMA\n')
            best_col, best_shape = random.choice(equal_best_placements)

        if best_col == None and best_shape == None:
            print('RANDOM GARA2 NONE\n')
            best_col, best_shape = (random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE]))
            
        best_movement = (best_col, best_shape) 
        print(best_movement)
        return best_movement