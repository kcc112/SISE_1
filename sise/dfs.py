from .node import Node, move

def solve_puzzle_dfs(node, directions, goal_node):
    stack_node = [node]
    current_depth = [0]
    max_depth = 20
    highest_depth = 0

    def dfs(route, depth):
        if depth[0] == max_depth:
            return
        if route.data.tolist() == goal_node.tolist():
            return route
        for direction in directions:
            new_data = move(direction, route.data)
            
            if new_data is not None and is_opposite_direction(direction, route.direction) is False:
                child_node = Node(new_data, route, direction)
                stack_node.append(child_node)
                depth[0] += 1
                next_route = dfs(stack_node[-1], depth)
                depth[0] -= 1
                if next_route:
                    return next_route

    while stack_node:
        route = dfs(stack_node[-1], current_depth)
        if current_depth[0] > highest_depth:
            highest_depth = current_depth[0]
        if route:
            return route, highest_depth
        else:
            stack_node.pop()
            current_depth[0] -= 1

    return None, highest_depth


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