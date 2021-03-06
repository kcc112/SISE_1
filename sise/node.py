import numpy as np

class Node:
    def __init__(self, data, parent, direction):
        self.data = data
        self.parent = parent
        self.direction = direction

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False


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


def is_opposite_direction(direction1, direction2):
    if direction1 == 'U' and direction2 == 'D':
        return True
    if direction1 == 'D' and direction2 == 'U':
        return True
    if direction1 == 'L' and direction2 == 'R':
        return True
    if direction1 == 'R' and direction2 == 'L':
        return True
    else:
        return False
