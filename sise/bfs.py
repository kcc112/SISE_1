from .node import Node, move

def solve_puzzle_bfs(node, directions, goal_node):
    node_queue = [node]
    visited_nodes = []
    visited_nodes.append(node_queue[0].data.tolist())
    node_counter = 0

    while node_queue:
        current_root = node_queue.pop(0)
        
        if current_root.data.tolist() == goal_node.tolist():
            return current_root

        for direction in directions:
            new_data = move(direction, current_root.data)

            if new_data is not None:
                node_counter += 1
                child_node = Node(node_counter, new_data, current_root, direction)

                if child_node.data.tolist() not in visited_nodes:
                    node_queue.append(child_node)
                    visited_nodes.append(child_node.data.tolist())
                    if child_node.data.tolist() == goal_node.tolist():
                        return child_node
    return None