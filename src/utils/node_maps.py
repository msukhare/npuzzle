import copy
import numpy as np

class node:
    def __init__(self, zero_pos, maps, move, before):
        self.g = 0
        self.h = 0
        self.f = 0
        self.y_zero = int(zero_pos[0])
        self.x_zero = int(zero_pos[1])
        self.move = move
        self.map = maps
        self.before = before

    def expand(self, moves):
        for m in moves:
            if self.x_zero + m[1][1] >= 0 and\
                self.x_zero + m[1][1] < self.map.shape[0] and\
                self.y_zero + m[1][0] >= 0 and\
                self.y_zero + m[1][0] < self.map.shape[0]:
                new_zero_y, new_zero_x = self.y_zero + m[1][0],\
                    self.x_zero + m[1][1]
                new_map = copy.deepcopy(self.map)
                new_map[self.y_zero][self.x_zero] = new_map[new_zero_y][new_zero_x]
                new_map[new_zero_y][new_zero_x] = 0
                yield node((new_zero_y, new_zero_x),\
                    new_map,\
                    m[0],\
                    self)

    def compute_f_score(self, heuristic, final_map, uniform, weight):
        if uniform is False:
            self.h = heuristic(self.map, final_map)
        self.f = self.g + self.h * weight

    def solved(self, final_map):
        return np.array_equal(self.map, final_map)

    def __eq__(self, to_cmp):
        return np.array_equal(self.map, to_cmp.map)

    def __hash__(self):
        return hash(self.map.tostring())

    def __lt__(self, to_cmp):
        if self.f < to_cmp.f:
            return True
        if self.f == to_cmp.f:
            if self.h < to_cmp.h:
                return True
        return False
