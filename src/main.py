import sys
import os
import argparse

from map_reader import MapReader, MapError
from utils import available_heuristics
from solver import aStarSolver

MOVES = (('UP', (-1, 0)), ('DOWN', (1, 0)), ('LEFT', (0, -1)), ('RIGHT', (0, 1)))

def main(parsed_args):
    global MOVES
    to_solve = MapReader(parsed_args.map_path)
    try:
        to_solve.read_map()
    except MapError as error_reading:
        sys.exit(str(error_reading))
    solver = aStarSolver(MOVES,\
            to_solve,\
            available_heuristics[parsed_args.heuristic],\
            parsed_args.greedy,\
            parsed_args.uniform,\
            parsed_args.weight)
    solver.run()
    solver.recap()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('map_path',\
            nargs='?',\
            type=str,\
            help="""correspond path to map or dir with maps""")
    parser.add_argument('--heuristic',\
            nargs='?',\
            type=str,\
            const='manhattan',\
            default='manhattan',\
            choices=['manhattan', 'hamming', 'count_tiles_out_of_rows_cols'],\
            help="""correspond to heuristic used in a*. By default manhattan""")
    parser.add_argument('--weight',\
            nargs='?',\
            type=float,\
            const=1.0,\
            default=1.0,\
            help="""correspond to weight to apply on heuristic in a*. By default weight is equal to 1""")
    parser.add_argument('--greedy',\
            dest='greedy',\
            action='store_true',\
            help="if pass as params a* make a greedy search, that means f function don't use g(x)")
    parser.add_argument('--uniform',\
            dest='uniform',\
            action='store_true',
            help="if pass as params a* make an uniform-cost search, that means f function don't use h(x)")
    parsed_args = parser.parse_args()
    if parsed_args.map_path is None:
        sys.exit("Error: missing name of map to use")
    if os.path.exists(parsed_args.map_path) is False:
        sys.exit("Error: %s doesn't exists" %parsed_args.map_path)
    if parsed_args.weight < 1:
        sys.exit("Error: weight must be sup or equal to 1")
    main(parsed_args)
