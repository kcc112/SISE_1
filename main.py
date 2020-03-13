import numpy as np
import argparse
import time
from sise import bfs, dfs, node, files_op


# Puzzle to solve

# mock_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 10, 11]])
# What we want at the end
# goal_node = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0]])
# goal_node = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
goal_node = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
directions = ['D', 'U', 'L', 'R']

parser = argparse.ArgumentParser()
   
parser.add_argument('-a', '--algorithm', help='Choose bfs or dfs astr', required=True)
parser.add_argument('-o', '--order', help='Choose order default: UDLR', required=False)
parser.add_argument('-f', '--file', help='File with start data', required=True)
parser.add_argument('-fs', '--file_solution', help='File with solution', required=False)
parser.add_argument('-fi', '--file_info', help='File with operation info', required=False)

args = parser.parse_args()

mock_data = files_op.parse_array_from_file(args.file)

root_node = node.Node(data=mock_data, parent=None, direction=None)

if args.order and sorted(args.order) == ['D', 'L', 'R', 'U']:
    directions = args.order

if args.algorithm == 'bfs':
  start = time.time()
  solution_bfs, visited_count, processed_count, max_depth = bfs.solve_puzzle_bfs(root_node, directions, goal_node)
  end = time.time()

  final_time = end - start

  if solution_bfs is None:
      print('Something went wrong')
      if args.file_solution:
        files_op.write_to_solution_file(args.file_solution, None)
        files_op.write_info_to_file(args.file_solution, None, final_time)
      else:
        files_op.write_to_solution_file('./files/solution.txt', None)
        files_op.write_info_to_file('./files/info.txt', None, final_time)
  else:
      print('Data before bfs:')
      print(str(mock_data))
      print('Data after bfs:')
      print(str(solution_bfs.data))
      print('Execution time')
      print(end - start)

      correct_moves = []
      while solution_bfs.parent is not None:
        correct_moves.append(solution_bfs.direction)
        solution_bfs = solution_bfs.parent

      correct_moves.reverse()
      if args.file_solution:
        files_op.write_to_solution_file( args.file_solution, correct_moves)
        files_op.write_info_to_file(args.file_solution, correct_moves, final_time)
      else:
        files_op.write_to_solution_file('./files/solution.txt', correct_moves)
        files_op.write_info_to_file('./files/info.txt', correct_moves, final_time)
      print('Moves list:')
      print(str(correct_moves))

elif args.algorithm == 'dfs':
  start = time.time()
  solution_dfs, highest_depth = dfs.solve_puzzle_dfs(root_node, directions, goal_node)
  end = time.time()

  final_time = end - start

  if solution_dfs is None:
      print('Something went wrong')
      if args.file_solution:
        files_op.write_to_solution_file(args.file_solution, None)
        files_op.write_info_to_file(args.file_solution, None, final_time)
      else:
        files_op.write_to_solution_file('./files/solution.txt', None)
        files_op.write_info_to_file('./files/info.txt', None, final_time)
  else:
      print('Data before dfs:')
      print(str(mock_data))
      print('Data after dfs:')
      print(str(solution_dfs.data))
      print('Execution time')
      print(end - start)

      correct_moves = []
      while solution_dfs.parent is not None:
        correct_moves.append(solution_dfs.direction)
        solution_dfs = solution_dfs.parent

      correct_moves.reverse()
      if args.file_solution:
        files_op.write_to_solution_file( args.file_solution, correct_moves)
        files_op.write_info_to_file(args.file_solution, correct_moves, final_time)
      else:
        files_op.write_to_solution_file('./files/solution.txt', correct_moves)
        files_op.write_info_to_file('./files/info.txt', correct_moves, final_time)
      print('Moves list:')
      print(str(correct_moves))