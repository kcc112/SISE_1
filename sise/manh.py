def calc_manh_dist(node):
    dist = 0
    height = len(node.data)
    if height == 0:
        return None
    width = len(node.data[0])
    for i in range(0, width):
        for j in range(0, height):
            correct_i = node.data[i][j] // 4
            correct_j = node.data[i][j] % 4
            dist += abs(correct_i - i)
            dist += abs(correct_j - j)
    return dist
