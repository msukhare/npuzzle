import numpy as np
import heapq

from utils import node

class aStarSolver:

    def __init__(self, moves, to_solve, heuristic, greedy, uniform, weight):
        self.moves = moves
        self.to_solve = to_solve
        self.heuristic = heuristic
        self.g_increment = int(greedy is False)
        self.uniform = uniform
        self.weight = weight
        self.path_of_solution = None
        self.open_set = {}
        self.closed_set = set()
        self.priority_queu = []
        self.time_complexity = 0
        self.space_complexity = 0

    def already_in_with_higher_cost(self, new):
        if self.open_set[new] <= new.f:
            return False
        for index, ele in enumerate(self.priority_queu):
            if ele == new:
                self.priority_queu.pop(index)
                return True
        return False

    def run(self):
        start = node(np.where(self.to_solve.map_to_solve == 0),\
                self.to_solve.map_to_solve,\
                'START',\
                None)
        start.g += self.g_increment
        start.compute_f_score(self.heuristic,\
                self.to_solve.final_map,\
                self.uniform,\
                self.weight)
        self.open_set[start] = start.f
        heapq.heappush(self.priority_queu, start)
        while (self.open_set):
            to_analyse = heapq.heappop(self.priority_queu)
            self.open_set.pop(to_analyse)
            self.closed_set.add(to_analyse)
            if to_analyse.solved(self.to_solve.final_map) is True:
                self.path_of_solution = to_analyse
                break
            for new in to_analyse.expand(self.moves):
                if new not in self.closed_set:
                    new.g = to_analyse.g + self.g_increment
                    new.compute_f_score(self.heuristic,\
                        self.to_solve.final_map,\
                        self.uniform,\
                        self.weight)
                    if new not in self.open_set or\
                        self.already_in_with_higher_cost(new) is True:
                        heapq.heappush(self.priority_queu, new)
                        self.open_set[new] = new.f
                        self.space_complexity = max(len(self.open_set),\
                            len(self.closed_set),\
                            self.space_complexity)
                        self.time_complexity += 1

    def show_all_path(self, current_node):
        all_path = []
        len_path = 0
        while (current_node is not None):
            all_path.insert(0, current_node)
            current_node = current_node.before
            len_path += 1
        for ele in all_path:
            print('---%s---' %ele.move)
            print(ele.map, '\n')
        print("Length of path: %d" %len_path)

    def recap(self):
        if self.path_of_solution is not None:
            self.show_all_path(self.path_of_solution)
        else:
            print("Any path was found")
        print("Time complexity: %d" %self.time_complexity)
        print("Space complexity: %d" %self.space_complexity)
