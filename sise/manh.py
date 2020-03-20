def calc_manh_dist(node):
    dist = 0
    height = len(node.data)
    if height == 0:
        return None
    width = len(node.data[0])
    for i in range(0, height):
        for j in range(0, width):
            correct_i = node.data[i][j] // width
            correct_j = node.data[i][j] % width
            dist += abs(correct_i - i)
            dist += abs(correct_j - j)
    return dist
