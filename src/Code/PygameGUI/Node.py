class Node:
    """
    A class representing a node in the A* algorithm.
    """
    def __init__(self, position: tuple, parent: "Node"=None):
        """
        Initialize a new Node instance.

        :param position:    The position of the node.
        :param parent:      The parent node of the node.
        """
        self.x, self.y = position # Coordinates of the node
        self.parent = parent # Parent node of the node
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic estimate of the cost from current node to the goal
        self.f = 0  # Total cost (g + h)

    def heuristic(self, node: "Node", goal: "Node") -> int:
        """
        Calculate the heuristic value of the node. The heuristic value is the Manhattan distance between the node and the goal.

        :param node:    The current node.
        :param goal:    The goal node.

        :return:        The heuristic value of the node.
        """
        return abs(node.x - goal.x) + abs(node.y - goal.y)

    def is_valid_cell(self, board: list, new_x: int, new_y: int) -> bool:
        """
        Check if the target square is a valid square. A square is valid if it is within the bounds of the map and is not a mountain.

        :param board:       The game board.
        :param new_x:       The x coordinate of the target square.
        :param new_y:       The y coordinate of the target square.

        :return:            A boolean representing whether the target square is a valid square or not.
        """
        return 0 <= new_x < len(board) and 0 <= new_y < len(board) and board[new_y][new_x] != "🗻"

    def get_neighboring_cells(self, board: list) -> "list['Node']":
        """
        Get the neighboring cells of the current node. 

        :param board:       The game board.
        :return:            A list of neighboring cells.
        """
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if self.is_valid_cell(board, new_x, new_y):
                neighbors.append(Node((new_x, new_y)))
        return neighbors

    def reconstruct_path(self, node) -> "list['tuple(int, int)']":
        """
        Reconstruct the path from the start node to the goal node.

        :param node:    The goal node.

        :return:        The path from the start node to the goal node.
        """
        path = [] # Path from the start node to the goal node
        while node:
            path.append((node.x, node.y))
            node = node.parent
        return path[::-1]

    def astar(self, board: list, goal: "Node") -> "list['tuple(int, int)']":
        """
        Perform the A* search algorithm to find a path from the start node to the goal node.

        :param board:       The game board.
        :param goal:        The goal node.

        :return:            The path from the start node to the goal node if a valid path is found, None otherwise.
        """
        open_set = [self]  # Nodes to be evaluated
        closed_set = set()  # Nodes already evaluated
        while open_set:
            current = min(open_set, key=lambda node: node.f)  # Node with the lowest f score
            if current.x == goal.x and current.y == goal.y:
                return self.reconstruct_path(current)  # Path found, return the reconstructed path
            open_set.remove(current)
            closed_set.add((current.x, current.y))
            neighbors = current.get_neighboring_cells(board)
            for neighbor in neighbors:
                if (neighbor.x, neighbor.y) in closed_set:
                    continue
                tentative_g = current.g + 1
                if neighbor not in open_set or tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor, goal)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current
                    if neighbor not in open_set:
                        open_set.append(neighbor)
        return None  # No path found