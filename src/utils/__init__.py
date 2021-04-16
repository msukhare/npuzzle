from .heuristics import manhattan_distance, hamming_distance, count_nouber_tiles_out_rows_cols
from .node_maps import node
from .solvability_checker import map_is_solvable


available_heuristics = {'manhattan': manhattan_distance,\
        'hamming': hamming_distance,\
        'count_tiles_out_of_rows_cols': count_nouber_tiles_out_rows_cols}
