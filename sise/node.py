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


def move_right(data, border):
    i, j = find_index(data)
    if j == border:
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


def move_down(data, border):
    i, j = find_index(data)
    if i == border:
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
      return move_down(data, data.shape[0] - 1)
    if direction == 'L':
      return move_left(data)
    if direction == 'R':
      return move_right(data, data.shape[1] - 1)
    else:
      return None