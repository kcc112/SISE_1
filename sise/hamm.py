from .node import Node


def calc_hamm_dist(node):
    dist = 0
    height = len(node.data)
    if height == 0:
        return None
    width = len(node.data[0])
    for i in range(0, height):
        for j in range(0, width):
            if node.data[i][j] != i*width + j:
                dist += 1
    return dist
