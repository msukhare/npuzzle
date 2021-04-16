import numpy as np
import heapq

from utils import node

class aStarSolver:

    def __init__(self, moves, to_solve, heuristic, weight=1):
        self.moves = moves
        self.to_solve = to_solve
        self.heuristic = heuristic
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
        start = node(1,\
                0,\
                np.where(self.to_solve.map_to_solve == 0),\
                self.to_solve.map_to_solve,\
                'START',\
                None)
        start.compute_f_score(self.heuristic(start.map,\
                self.to_solve.final_map),\
                self.weight)
        self.open_set[start] = start.f
        heapq.heappush(self.priority_queu, start)
        while (self.open_set):
            to_analyse = heapq.heappop(self.priority_queu)
            self.open_set.pop(to_analyse)
            self.closed_set.add(to_analyse)
            if to_analyse.h == 0:
                self.path_of_solution = to_analyse
                return
            for new in to_analyse.expand(self.moves):
                if new not in self.closed_set:
                    new.compute_f_score(self.heuristic(new.map,\
                            self.to_solve.final_map),\
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
        if current_node is not None:
            self.show_all_path(current_node.before)
            print('---%s---' %current_node.move)
            print(current_node.map, '\n')

    def recap(self):
        if self.path_of_solution is not None:
            #self.show_all_path(self.path_of_solution)
            print("Length of path: %d" %self.path_of_solution.g)
        else:
            print("Any path was found")
        print("Time complexity: %d" %self.time_complexity)
        print("Space complexity: %d" %self.space_complexity)
