import numpy as np

def flatten_in_order(map_to_solve, final_map, size_map):
    to_ret = []
    for i in range(1, size_map**2):
        y, x = np.where(final_map == i)
        to_ret.append(map_to_solve[y, x])
    y, x = np.where(final_map == 0)
    tmp = map_to_solve[y, x]
    if tmp != 0:
        to_ret.append(tmp)
    return to_ret

def count_inversions(flatten_map):
    number_inversion = 0
    for i in range(len(flatten_map)):
        for j in range(i + 1, len(flatten_map)):
            if flatten_map[i] != 0 and\
                flatten_map[j] != 0 and\
                flatten_map[i] > flatten_map[j]:
                number_inversion += 1
    return number_inversion

def map_is_solvable(map_to_solve, final_map, map_size):
    number_inversion = count_inversions(flatten_in_order(map_to_solve, final_map, map_size))
    y_zero_pos = 0
    if map_size % 2 == 0:
        y, x = np.where(map_to_solve == 2)
        number_inversion += int(y)
        y_zero_pos += int(y)
    if number_inversion % 2 == y_zero_pos % 2:
        return True
    return False
