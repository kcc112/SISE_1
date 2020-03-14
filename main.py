import numpy as np
import argparse
import time
from sise import bfs, dfs, node, files_op, manh, hamm, astar


# Puzzle to solve

# mock_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 10, 11]])
# What we want at the end
# goal_node = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0]])
# goal_node = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
goal_node = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
directions = ['D', 'U', 'L', 'R']

parser = argparse.ArgumentParser()
   
parser.add_argument('-a', '--algorithm', help='Choose bfs, dfs, manh or hamm', required=True)
parser.add_argument('-o', '--order', help='Choose order default: UDLR', required=False)
parser.add_argument('-f', '--file', help='File with start data', required=True)
parser.add_argument('-fs', '--file_solution', help='File with solution', required=False)
parser.add_argument('-fi', '--file_info', help='File with operation info', required=False)

args = parser.parse_args()

mock_data = files_op.parse_array_from_file(args.file)

root_node = node.Node(data=mock_data, parent=None, direction=None)

if args.order and sorted(args.order) == ['D', 'L', 'R', 'U']:
    directions = args.order
used_algorithm = None
solution, max_depth = (0, 0)
start = time.time()

if args.algorithm == 'bfs':
    solution, max_depth = bfs.solve_puzzle_bfs(root_node, directions, goal_node)
elif args.algorithm == 'dfs':
    solution, max_depth = dfs.solve_puzzle_dfs(root_node, directions, goal_node)
elif args.algorithm == 'manh':
    solution, max_depth = astar.solve_puzzle_astar(root_node, manh.calc_manh_dist)
elif args.algorithm == 'hamm':
    solution, max_depth = astar.solve_puzzle_astar(root_node, hamm.calc_hamm_dist)

end = time.time()

final_time = end - start

if solution is None:
    print('Something went wrong')
    if args.file_solution:
        files_op.write_to_solution_file(args.file_solution, None)
        files_op.write_info_to_file(args.file_solution, None, final_time)
    else:
        files_op.write_to_solution_file('./files/solution.txt', None)
        files_op.write_info_to_file('./files/info.txt', None, final_time)
else:
    print('Data before solving:')
    print(str(mock_data))
    print('Data after solving:')
    print(str(solution.data))
    print('Execution time')
    print(end - start)

    correct_moves = []
    while solution.parent is not None:
        correct_moves.append(solution.direction)
        solution = solution.parent

    correct_moves.reverse()
    if args.file_solution:
        files_op.write_to_solution_file(args.file_solution, correct_moves)
        files_op.write_info_to_file(args.file_solution, correct_moves, final_time)
    else:
        files_op.write_to_solution_file('./files/solution.txt', correct_moves)
        files_op.write_info_to_file('./files/info.txt', correct_moves, final_time)
    print('Moves list:')
    print(str(correct_moves))