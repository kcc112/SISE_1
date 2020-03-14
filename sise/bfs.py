from .node import Node, move

def solve_puzzle_bfs(node, directions, goal_node):
    max_depth = 20
    node.cur_depth = 0
    node_queue = [node]
    visited_nodes = [node_queue[0].data.tolist()]

    while node_queue:
        current_root = node_queue.pop(0)
        
        if current_root.data.tolist() == goal_node.tolist():
            return current_root, current_root.cur_depth
        if current_root.cur_depth != max_depth:
            for direction in directions:
                new_data = move(direction, current_root.data)

                if new_data is not None:
                    child_node = Node(new_data, current_root, direction)
                    child_node.cur_depth = current_root.cur_depth + 1

                    if child_node.data.tolist() not in visited_nodes:
                        node_queue.append(child_node)
                        visited_nodes.append(child_node.data.tolist())
                        if child_node.data.tolist() == goal_node.tolist():
                            return child_node, child_node.cur_depth

    return None, max_depth
