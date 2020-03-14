import heapq
from sise import node


def solve_puzzle_astar(root_node, heuristic):
    priority_queue = []
    depth = 0
    heapq.heappush(priority_queue, (heuristic(root_node), 0, root_node))
    highest_depth = 0

    def astar_step(current_node):
        if heuristic(current_node) == 0:
            return current_node
        for direction in ['D', 'L', 'U', 'R']:
            new_data = node.move(direction, current_node.data)

            if new_data is not None and node.is_opposite_direction(direction, current_node.direction) is False:
                child_node = node.Node(new_data, current_node, direction)
                heapq.heappush(priority_queue, (heuristic(child_node), depth + 1, child_node))
        return None

    while True:
        heuristic_value, depth, next_node = heapq.heappop(priority_queue)
        if highest_depth < depth:
            highest_depth = depth
        solution_node = astar_step(next_node)

        if solution_node is not None:
            return solution_node, depth


