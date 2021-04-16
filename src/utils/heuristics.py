import numpy as np

def manhattan_distance(actual_map, final_map):
    distance = 0
    for i in range(final_map.shape[0]):
        for j in range(final_map.shape[1]):
            if final_map[i][j] != 0:
                where_ele = np.where(final_map[i][j] == actual_map)
                distance += (np.abs(where_ele[1] - j) + np.abs(where_ele[0] - i))
    return int(distance)

def hamming_distance(actual_map, final_map):
    nb = 0
    for i in range(actual_map.shape[0]):
        for j in range(actual_map.shape[1]):
            if actual_map[i][j] != 0 and\
                actual_map[i][j] != final_map[i][j]:
                nb += 1
    return nb

def count_nouber_tiles_out_rows_cols(actual_map, final_map):
    count = 0
    for i in range(1, actual_map.shape[0]**2):
        where_actual_tile_row, where_actual_tile_col = np.where(actual_map == i)
        where_goal_tile_row, where_goal_tile_col = np.where(final_map == i)
        if where_actual_tile_row != where_goal_tile_row:
            count += 1
        if where_actual_tile_col != where_goal_tile_col:
            count += 1
    return count
