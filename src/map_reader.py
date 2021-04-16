import numpy as np

from utils import map_is_solvable

class MapError(ValueError):
    """Raise when something wrong with map like bad format or map is unsolvable"""

class MapReader:

    def __init__(self, path_to_map):
        self.path_to_map = path_to_map
        self.map_size = 0
        self.map_to_solve = []
        self.final_map = []

    def generate_final_map(self):
        self.final_map = np.zeros((self.map_size, self.map_size), dtype=np.int)
        x, y = 0, 0
        incre_x, incre_y = 1, 0
        for i in range(1, self.map_size**2):
            self.final_map[y][x] = i
            next_x, next_y = x + incre_x, y + incre_y
            if next_x >= 0 and next_x < self.map_size and\
                next_y >= 0 and next_y < self.map_size and\
                self.final_map[next_y][next_x] == 0:
                x, y = next_x, next_y
            else:
                incre_x, incre_y = -incre_y, incre_x
                x, y = x + incre_x, y + incre_y

    def all_tiles_are_presents(self):
        map_to_check = [ele for row in self.map_to_solve for ele in row]
        for ele in range(self.map_size**2):
            if ele not in map_to_check:
                return False
        return True

    def transform_line(self, line, index):
        line = line.split('#')[0].replace('\n', '').replace('\t', ' ').split(' ')
        new_line = []
        for ele in line:
            if ele:
                if ele.isdigit() is False:
                    raise MapError("Error: in %s on line %d, map only must contains only digit"
                        %(self.path_to_map, index))
                new_line.append(int(ele))
        return new_line

    def parse_map(self, data):
        i = 0
        while (i < len(data) and self.map_size == 0):
            line = self.transform_line(data[i], i)
            if line and len(line) == 1:
                self.map_size = int(line[0])
                if self.map_size < 3:
                    raise MapError("Error: size map must be superior or equal to three in %s"\
                        %self.path_to_map)
            elif line:
                raise MapError("Error: map size must be first in %s"\
                    %self.path_to_map)
            i += 1
        for i in range(i, len(data)):
            line = self.transform_line(data[i], i)
            if line:
                if len(line) == self.map_size:
                    self.map_to_solve.append(line)
                else:
                    raise MapError("""Error: in %s error on line %d, number of cols (%d) in on row must
                        be equal to size of map (%d)""" %(self.path_to_map,\
                        self.map_size, len(line), self.map_size))

    def read_map(self):
        with open(self.path_to_map, 'r') as fd:
            self.parse_map(fd.read().split('\n'))
        if self.map_size == 0:
            raise MapError("Error: missing map size in file in %s" %self.path_to_map)
        if self.map_size != len(self.map_to_solve):
            raise MapError("Error: number of rows (%d) must be equal to size map (%d) in %s"
                %(len(self.map_to_solve), self.map_size, self.path_to_map))
        if self.all_tiles_are_presents() is False:
            raise MapError("Error: somes values seems doesn't correspond to size map (%d)"
                %self.map_size)
        self.map_to_solve = np.asarray(self.map_to_solve)
        self.generate_final_map()
        if map_is_solvable(self.map_to_solve, self.final_map, self.map_size) is False:
            raise MapError("Error: map in %s is unsolvable" %self.path_to_map)

