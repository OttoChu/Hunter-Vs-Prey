def a_star_pathfinding(game_map, start_pos, end_pos):
    # Define a heuristic function
    def heuristic(pos):
        if game_map[pos[0]][pos[1]] == "M":
            return float('inf')
        return abs(pos[0]-end_pos[0]) + abs(pos[1]-end_pos[1])

    # Initialize the start node
    start_node = {
        "pos": start_pos,
        "g": 0,
        "f": heuristic(start_pos),
        "parent": None
    }

    # Initialize the open and closed sets
    open_set = [start_node]
    closed_set = []

    # Iterate until there are no more nodes in the open set
    while len(open_set) > 0:
        # Get the node with the lowest f value from the open set
        current_node = min(open_set, key=lambda x: x["f"])

        # Check if we have reached the end position
        if current_node["pos"] == end_pos:
            # Construct the path from the start to the end
            path = []
            while current_node:
                path.append(current_node["pos"])
                current_node = current_node["parent"]
            path.reverse()
            return path

        # Remove the current node from the open set and add it to the closed set
        open_set.remove(current_node)
        closed_set.append(current_node)

        # Generate the successors of the current node
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current_node["pos"][0]+dx, current_node["pos"][1]+dy
            if (new_x >= 0 and new_x < len(game_map) and new_y >= 0 and new_y < len(game_map[0])) and game_map[new_x][new_y] != "🗻":
                successor_pos = (new_x, new_y)
                successor_g = current_node["g"] + 1
                successor_f = successor_g + heuristic(successor_pos)
                successor_node = {
                    "pos": successor_pos,
                    "g": successor_g,
                    "f": successor_f,
                    "parent": current_node
                }

                # Check if the successor node is already in the closed set
                in_closed_set = False
                for node in closed_set:
                    if node["pos"] == successor_pos:
                        in_closed_set = True
                        break

                # Check if the successor node is already in the open set
                in_open_set = False
                for node in open_set:
                    if node["pos"] == successor_pos:
                        in_open_set = True
                        if node["g"] > successor_g:
                            node["g"] = successor_g
                            node["f"] = successor_f
                            node["parent"] = current_node
                        break

                # Add the successor node to the open set if it is not already in the open or closed set
                if not in_closed_set and not in_open_set:
                    open_set.append(successor_node)

    # If we get here, there is no path from the start to the end
    return None