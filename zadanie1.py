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

def solve_puzzle_dfs(node, directions, goal_node):
    node_stack = [node]
    max_depth = 20
    current_depth = 0
    visited_nodes = []
    visited_nodes.append(node_stack[0].data.tolist())
    node_counter = 0

    while node_stack:
        current_root = node_stack[-1]
        
        if current_root.data.tolist() == goal_node.tolist():
            return current_root

        new_data = 0    

        while current_depth != max_depth and new_data is not None:
            for direction in directions:
                new_data = move(direction, current_root.data)

                if new_data is not None:
                    node_counter += 1
                    child_node = Node(node_counter, new_data, current_root, direction)

                    if child_node.data.tolist() not in visited_nodes:
                        node_stack.append(child_node)
                        visited_nodes.append(child_node.data.tolist())
                        current_root = node_stack[-1]
                    if child_node.data.tolist() == goal_node.tolist():
                        return child_node

        node_stack.pop()
        current_depth -= 1

    return None


######################################################

# Puzzle to solve
mock_data = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
# What we want at the end
goal_node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
directions = ['D', 'U', 'L', 'R']

root_node = Node(node_number=0, data=mock_data, parent=None, direction=None)

solution_bfs = solve_puzzle_bfs(root_node, directions, goal_node)
solution_dfs = solve_puzzle_dfs(root_node, directions, goal_node)

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

    print(str(correct_moves))

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

    print(str(correct_moves))