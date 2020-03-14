from sise import node


def solve_puzzle_dfs(root_node, directions, goal_node):
    stack_node = [root_node]
    current_depth = [0]
    max_depth = 20
    highest_depth = 0

    def dfs(route, depth):
        if depth[0] == max_depth:
            return
        if route.data.tolist() == goal_node.tolist():
            return route
        for direction in directions:
            if node.is_opposite_direction(direction, route.direction):
                continue
            new_data = node.move(direction, route.data)
            
            if new_data is not None:
                child_node = node.Node(new_data, route, direction)
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