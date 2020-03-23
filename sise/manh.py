import numpy as np


def calc_manh_dist(node, root_node):
    dist = 0
    height = len(node.data)
    if height == 0:
        return None
    width = len(node.data[0])
    for i in range(0, height):
        for j in range(0, width):
            # calculate dist from current to goal
            correct_i = node.data[i][j] // width
            correct_j = node.data[i][j] % width
            dist += abs(correct_i - i)
            dist += abs(correct_j - j)
            # calculate dist from current to root
            current_value_at = np.where(root_node.data == node.data[i][j])
            dist += abs(current_value_at[0][0] - i)
            dist += abs(current_value_at[1][0] - j)
    return dist
