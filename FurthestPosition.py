def furthest_position(game_map, target_pos, current_pos=None):
    # Initialize a 2D array to store the distances from the target position
    distances = [[float('inf') if game_map[i][j] == "M" else -1 for j in range(len(game_map[0]))] for i in range(len(game_map))]
    distances[target_pos[0]][target_pos[1]] = 0

    # Use a queue to perform a flood fill starting from the target position
    queue = [target_pos]
    while len(queue) > 0:
        pos = queue.pop(0)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = pos[0]+dx, pos[1]+dy
            if (new_x >= 0 and new_x < len(game_map) and new_y >= 0 and new_y < len(game_map[0])) and game_map[new_x][new_y] != "M":
                if distances[new_x][new_y] == -1:
                    distances[new_x][new_y] = distances[pos[0]][pos[1]] + 1
                    queue.append((new_x, new_y))

    # Find the position with the maximum distance from the target position
    max_distance = -1
    max_pos = None
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] != "🗻" and distances[i][j] > max_distance:
                max_distance = distances[i][j]
                max_pos = (i, j)

    # Check if the current position is farther away from the target than the furthest position found
    if current_pos is not None:
        current_distance = distances[current_pos[0]][current_pos[1]]
        if current_distance > max_distance:
            max_pos = current_pos

    return max_pos