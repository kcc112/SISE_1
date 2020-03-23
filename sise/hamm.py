from .node import Node


def calc_hamm_dist(node, root_node):
    dist = 0
    height = len(node.data)
    if height == 0:
        return None
    width = len(node.data[0])
    for i in range(0, height):
        for j in range(0, width):
            if node.data[i][j] != i*width + j:
                dist += 1  # calculate dist from current to goal
            if node.data[i][j] != root_node.data[i][j]:
                dist += 1  # calculate dist from current to root
    return dist
