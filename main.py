import numpy as np
import argparse
from sise import bfs, dfs, node


# Puzzle to solve
mock_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [0, 13, 14, 15]])
# What we want at the end
goal_node = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
directions = ['D', 'U', 'L', 'R']

parser = argparse.ArgumentParser()
   
parser.add_argument('-a', '--algorithm', help='Choose bfs or dfs astr', required=True)
parser.add_argument('-o', '--order', help='Choose order default: UDLR', required=False)

args = parser.parse_args()

root_node = node.Node(node_number=0, data=mock_data, parent=None, direction=None)


if args.order and sorted(args.order) == ['D', 'L', 'R', 'U']:
    directions = args.order

if args.algorithm == 'bfs':
  solution_bfs = bfs.solve_puzzle_bfs(root_node, directions, goal_node)

  if solution_bfs is None:
      print('Something went wrong')
  else:
      print('Data before bfs:')
      print(str(mock_data))
      print('Data after bfs:')
      print(str(solution_bfs.data))

      correct_moves = []
      while solution_bfs.parent is not None:
        correct_moves.append(solution_bfs.direction)
        solution_bfs = solution_bfs.parent

      correct_moves.reverse()

      print('Moves list:')
      print(str(correct_moves))

elif args.algorithm == 'dfs':
  solution_dfs = dfs.solve_puzzle_dfs(root_node, directions, goal_node)

  if solution_dfs is None:
      print('Something went wrong')
  else:
      print('Data before dfs:')
      print(str(mock_data))
      print('Data after dfs:')
      print(str(solution_dfs.data))

      correct_moves = []
      while solution_dfs.parent is not None:
        correct_moves.append(solution_dfs.direction)
        solution_dfs = solution_dfs.parent

      correct_moves.reverse()

      print('Moves list:')
      print(str(correct_moves))