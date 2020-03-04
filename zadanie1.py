import numpy as np

class Node:
    def __init__(self, node_number, data, parent, direction):
        self.data = data
        self.parent = parent
        self.direction = direction
        self.node_number = node_number


def find_index(array):
    i, j = np.where(array == 0)
    i = int(i)
    j = int(j)
    return i, j


def move_left(data):
    i, j = find_index(data)
    if j == 0:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i, j - 1]
        temp_arr[i, j] = temp
        temp_arr[i, j - 1] = 0
        return temp_arr


def move_right(data):
    i, j = find_index(data)
    if j == 2:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i, j + 1]
        temp_arr[i, j] = temp
        temp_arr[i, j + 1] = 0
        return temp_arr


def move_up(data):
    i, j = find_index(data)
    if i == 0:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i - 1, j]
        temp_arr[i, j] = temp
        temp_arr[i - 1, j] = 0
        return temp_arr


def move_down(data):
    i, j = find_index(data)
    if i == 2:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i + 1, j]
        temp_arr[i, j] = temp
        temp_arr[i + 1, j] = 0
        return temp_arr


def move(direction, data):
    if direction == 'U':
      return move_up(data)
    if direction == 'D':
      return move_down(data)
    if direction == 'L':
      return move_left(data)
    if direction == 'R':
      return move_right(data)
    else:
      return None


def solve_puzzle_bfs(node, directions, goal_node):
    node_queue = [node]
    visited_nodes = []
    visited_nodes.append(node_queue[0].data.tolist())
    node_counter = 0

    while node_queue:
        current_root = node_queue.pop(0)
        
        if current_root.data.tolist() == goal_node.tolist():
            return current_root

        for direction in directions:
            new_data = move(direction, current_root.data)

            if new_data is not None:
                node_counter += 1
                child_node = Node(node_counter, new_data, current_root, direction)

                if child_node.data.tolist() not in visited_nodes:
                    node_queue.append(child_node)
                    visited_nodes.append(child_node.data.tolist())
                    if child_node.data.tolist() == goal_node.tolist():
                        return child_node
    return None

# Puzzle to solve
mock_data = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
# What we want at the end
goal_node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
directions = ['D', 'U', 'L', 'R']

root_node = Node(node_number=0, data=mock_data, parent=None, direction=None)

solution = solve_puzzle_bfs(root_node, directions, goal_node)

if solution is None:
    print('Something went wrong')
else:
    print('Data before:')
    print(str(mock_data))
    print('Data after:')
    print(str(solution.data))

    correct_moves = []
    while solution.parent is not None:
      correct_moves.append(solution.direction)
      solution = solution.parent

    correct_moves.reverse()

    print(str(correct_moves))