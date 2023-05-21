# Hunter Vs Prey v1.4.2

from random import randint
from time import sleep
import os
from termcolor import cprint, colored as coloured
import msvcrt


T = Tree = "🌳"
P = Prey = "🦊"
H = Hunter = "👨"
M = Mountain = "🗻"
F = Fog = "⬜"


class Game:
    """
    The main class that runs the game.
    """
    def __init__(self):
        """
        Initialize the game.
        """
        self.game_over = False # A boolean that indicates whether the game is over or not.
        self.moves = 0 # The number of moves the player has made.
    
    def homepage(self) -> int:
        """
        Print the homepage onto the screen. Ask for input for what to show next.

        :return: A number between 1 - 3 representing the chosen option.
        """
        cprint("Welcome to Hunter Vs Prey!", "green", attrs=["bold"])
        print()
        cprint("How to win?", "blue")
        cprint("The goal of this game is to get the hunter to the prey.", "blue")
        print()
        print(coloured("1. ", "black") + coloured("Rules", "yellow"))
        print(coloured("2. ", "black") + coloured("New Game", "yellow"))
        print(coloured("3. ", "black") + coloured("Quit", "yellow"))
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if option == 3:
                        print("Thank you for playing!")
                        raise SystemExit
                    return option
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def rules(self):
        """
        Print all the rules onto the screen.
        """
        print("Rules")
        print("1. Squares that you can be on are represented as 🌳.")
        print("2. Squares that you can **NOT** be on are represented as 🗻.")
        print("3. The Prey is represented as 👨.")
        print("4. The Hunter is represented as 🦊.")
        print("5. If an invalid move is made, your total move will be " + coloured("incremented by 1", "red") + "!")
        print("6. You starts with 10 special moves.")
        print("7. Toggling your special move will count as a turn.")
        print()
        print('Here are the accepted inputs:')
        cprint("'W' to move upwards", 'red')
        cprint("'A' to move to the left", 'blue')
        cprint("'S' to move downwards", 'yellow')
        cprint("'D' to move to the right", 'magenta')
        print()
        cprint("'E' to toggle the special move", "green")
        print()
        cprint("Press anything to return to the homepage.", "black")
        _ = msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')

    def end(self) -> bool:
        """
        Print the end screen onto the screen. Ask for input for whether to play again.

        :return: A boolean that indicates whether the player wants to play again.
        """
        self.game_over = True
        os.system('cls' if os.name == 'nt' else 'clear')
        cprint("The hunter has eaten the prey!", "green", "on_red")
        cprint(" __     ______  _    _  __          _______ _   _   _ \n \ \   / / __ \| |  | | \ \        / /_   _| \ | | | |\n  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | | |\n   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | | |\n    | | | |__| | |__| |    \  /\  /   _| |_| |\  | |_|\n    |_|  \____/ \____/      \/  \/   |_____|_| \_| (_)\n", "red")
        print(f"You caught the prey in {self.moves} moves")
        print("Play again? (Y/N)")
        print()
        while True:
            again = msvcrt.getch()
            try:
                again = again.decode("utf-8").upper()
                if again == 'Y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True
                elif again == 'N':
                    print("Thank you for playing!")
                    return False
            except UnicodeDecodeError:
                pass
            cprint("Wrong input! Try again!", "red")

    def ask_difficulty(self) -> int:
        """
        Ask the user for the game difficulty.
        
        :return: A number between 1 - 5 representing the chosen difficulty.
        """
        print("Game difficulties:")
        print(coloured("1. ", "black") + coloured("Extra Easy", "cyan"))
        print(coloured("2. ", "black") + coloured("Easy", "light_blue"))
        print(coloured("3. ", "black") + coloured("Normal", "light_yellow"))
        print(coloured("4. ", "black") + coloured("Hard", "light_red"))
        print(coloured("5. ", "black") + coloured("Extra Hard", "light_magenta"))
        print()
        print("Please enter game difficulty:")
        while True:
            difficulty = msvcrt.getch()
            try:
                difficulty = int(difficulty.decode("utf-8"))
                if difficulty > 0 and difficulty <= 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return difficulty
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")
            
    def ask_move(self) -> str:
        """
        Ask the user for the next move.
        """
        while True:
            move = msvcrt.getch()
            try:
                move = move.decode("utf-8").upper()
                if move == 'W' or move == 'A' or move == 'S' or move == 'D' or move == 'E':
                    self.moves += 1
                    return move
            except UnicodeDecodeError:
                pass
            cprint("Wrong input! Try again!", "red")


class GameMap:
    def __init__(self, size: int):
        """
        Initialize the game map.

        :param size:    The size of the map.
        """
        self.size = size

    def setup_map(self, difficulty: int) -> tuple:
        """
        Generates a new map with the Hunter and Prey.

        :param difficulty:  A number between 1(easiest) - 5(hardest) representing the chosen difficulty.

        :return: A tuple of the coordinates of the Hunter and Prey.
        """
        if difficulty == 1: # Extra Easy
            self.game_map = [[M for _ in range(self.size)] for _ in range(self.size)]
            self.game_map[1][1] = H
            self.game_map[1][2] = P
            return ((1,1), (2,1))
        # Fill get the border of the map with mountains
        self.game_map = [[M for _ in range(self.size)] if i == 0 or i == self.size - 1 else [
            M if i == 0 or i == self.size - 1 else T for i in range(self.size)] 
            for i in range(self.size)]
        # Add mountains to the map randomly based on the difficulty chosen
        number_of_mountains = int(self.size * (6 - difficulty) / 2)
        for i in range(number_of_mountains):
            while (True):
                x = randint(1, self.size - 1)
                y = randint(1, self.size - 1)
                if self.game_map[y][x] != M:
                    self.game_map[y][x] = M
                    if self.is_map_reachable():
                        break
                    else:
                        self.game_map[y][x] = T
        while True:  # Add the Hunter onto the map
            hunter_x = randint(1, self.size - 1)
            hunter_y = randint(1, self.size - 1)
            if self.game_map[hunter_y][hunter_x] != M:
                self.game_map[hunter_y][hunter_x] = H
                break
        dots = 0
        while True:  # Add the Prey onto the map while showing a "loading screen"
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Generating new map" + dots * '.')
            sleep(0.5)
            dots += 1
            if dots > 3:
                dots = 0
            prey_x = randint(1, self.size - 1)
            prey_y = randint(1, self.size - 1)
            if self.game_map[prey_y][prey_x] != M and (prey_x, prey_y) != (hunter_x, hunter_y):
                self.game_map[prey_y][prey_x] = P
                break
        os.system('cls' if os.name == 'nt' else 'clear')
        return (hunter_x, hunter_y), (prey_x, prey_y)
    
    def is_map_reachable(self):
        """
        Check if the map is reachable.

        :return: True if the map is reachable, False otherwise.
        """
        # Convert 2D array to graph
        graph = {}
        rows, cols = len(self.game_map), len(self.game_map[0])
        for i in range(rows):
            for j in range(cols):
                if self.game_map[i][j] != M:
                    neighbors = []
                    if i > 0 and self.game_map[i-1][j] != M:
                        neighbors.append((i-1, j))
                    if i < rows-1 and self.game_map[i+1][j] != M:
                        neighbors.append((i+1, j))
                    if j > 0 and self.game_map[i][j-1] != M:
                        neighbors.append((i, j-1))
                    if j < cols-1 and self.game_map[i][j+1] != M:
                        neighbors.append((i, j+1))
                    graph[(i, j)] = neighbors
        # Traverse graph to check reachability
        visited = set()
        start_node = next(iter(graph))  # Choose an arbitrary node as starting point
        self.depth_first_search(start_node, graph, visited)
        return len(visited) == len(graph)
    
    def depth_first_search(self, node: tuple, graph: dict, visited: set):
        """
        Traverse the graph using depth-first search.

        :param node:        The current node.
        :param graph:       The graph to traverse.
        :param visited:     A set of visited nodes.

        :return: A set of visited nodes.
        """
        visited.add(node) # Mark the current node as visited
        for neighbor in graph[node]: # Recursively visit all unvisited neighbors
            if neighbor not in visited:
                self.depth_first_search(neighbor, graph, visited)

    def print_game_state(self, hunter: Hunter, moves: int, fog: bool = False):
        """
        Print the map with the charges left to the screen.
        If fog is enabled, only the 5x5 area around the Hunter is shown.

        :param hunter:  The current Hunter instance.
        :param moves:   The number of moves the Hunter has made.
        :param fog:     A boolean showing wether the fog of war is enabled.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        if fog:
            # TODO: Implement fog of war
            pass
        for each_row in self.game_map:
            line = ""
            for each_item in each_row:
                line += each_item + ' '
            print(line)
        print()
        print("You have " + coloured(str(hunter.charges), "red", attrs=["bold"]) + " charge(s) left!")
        if hunter.speed == 2:
            print("You " + coloured("are", "red", attrs=["bold"]) + " currently using a charge.")
        else:
            print("You " + coloured("are not", "red", attrs=["bold"]) + " currently using a charge.")
        print()
        print("This is your " + coloured(f"{moves}th ", "green") + "move.")
        cprint("This will not update until you made a valid move!", "red")

    def is_mountain(self, x: int, y: int) -> bool:
        """
        Check if the target square is a mountain.

        :param x:   The x coordinate of the target square.
        :param y:   The y coordinate of the target square.

        :return:    A boolean representing whether the target square is a mountain or not.
        """
        return self.game_map[y][x] == M

    def update(self, old_x: int, old_y: int, new_x: int, new_y: int, target: str):
        """
        Update the map with the new position of the Hunter.

        :param old_x:   The old x coordinate of the Hunter.
        :param old_y:   The old y coordinate of the Hunter.
        :param new_x:   The new x coordinate of the Hunter.
        :param new_y:   The new y coordinate of the Hunter.
        :param target:  The target square to move to.
        """
        self.game_map[new_y][new_x] = target
        self.game_map[old_y][old_x] = T


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

    def is_valid_cell(self, game_map: GameMap, new_x: int, new_y: int) -> bool:
        """
        Check if the target square is a valid square. A square is valid if it is within the bounds of the map and is not a mountain.

        :param game_map:    The GameMap object.
        :param new_x:       The x coordinate of the target square.
        :param new_y:       The y coordinate of the target square.

        :return:            A boolean representing whether the target square is a valid square or not.
        """
        return 0 <= new_x < game_map.size and 0 <= new_y < game_map.size and game_map.game_map[new_y][new_x] != "🗻"

    def get_neighboring_cells(self, game_map: GameMap) -> "list['Node']":
        """
        Get the neighboring cells of the current node. 

        :param game_map:    The GameMap object.

        :return:            A list of neighboring cells.
        """
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if self.is_valid_cell(game_map, new_x, new_y):
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

    def astar(self, game_map: GameMap, goal: "Node") -> "list['tuple(int, int)']":
        """
        Perform the A* search algorithm to find a path from the start node to the goal node.

        :param game_map:    The GameMap object.
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
            neighbors = current.get_neighboring_cells(game_map)
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


class Animal():
    """
    A class representing an animal.
    """
    def __init__(self, x: int, y: int):
        """
        Initialize a new Animal instance.
        
        :param x:   The x coordinate of the animal.
        :param y:   The y coordinate of the animal.
        """
        self.x = x
        self.y = y
        self.speed = 1 # The speed of the animal


class Hunter(Animal):
    """
    A class representing a hunter.
    """
    def __init__(self, coordinate: tuple):
        """
        Initialize a new Hunter instance.

        :param coordinate:  The coordinate of the hunter.
        """
        self.charges = 10 # The number of special charges the hunter has
        super().__init__(coordinate[0], coordinate[1])

    def set_coordinate(self, coordinate: tuple):
        """
        Store a new coordinate for the hunter.

        :param coordinate:  The new coordinate for the hunter.
        """
        self.x = coordinate[0]
        self.y = coordinate[1]

    def toggle(self) -> bool:
        """
        Toggle the speed of the hunter.

        :return:    A boolean representing whether the speed of the hunter is toggled or not.
        """
        if self.charges <= 0:
            self.speed = 1
            return False
        if self.speed == 1:
            self.speed = 2
        else:
            self.speed = 1
        return True


class Prey(Animal):
    """
    A class representing a prey.
    """
    def __init__(self, coordinate: tuple):
        """
        Initialize a new Prey instance.

        :param coordinate:  The coordinate of the prey.
        
        """
        self.breathing = True
        super().__init__(coordinate[0], coordinate[1])

    def set_coordinate(self, coordinate: tuple):
        """
        Store a new coordinate for the prey.

        :param coordinate:  The new coordinate for the prey.
        """
        self.x = coordinate[0]
        self.y = coordinate[1]

    def make_move(self, game_map: GameMap, hunter_pos:tuple):
        """
        Make a move for the prey.

        :param game_map:    The GameMap object.
        :param hunter_pos:  The position of the hunter.

        :return:            The new position of the prey.
        """
        possible_moves = [(self.x-1, self.y), (self.x+1, self.y), (self.x, self.y-1), (self.x, self.y+1)]
        distances, trash_moves, trash_distances = [], [], [] # Lists to store the distances and invalid moves
        # Setting up the node for the current prey position and the hunter position
        current_node = Node((self.x, self.y))
        hunter_node = Node(hunter_pos)
        current_distance = len(current_node.astar(game_map, hunter_node))
        # Remove add the invalid moves to a separate list
        for i, each in enumerate(possible_moves):
            if game_map.game_map[each[1]][each[0]] == M or game_map.game_map[each[1]][each[0]] == H:
                trash_moves.append(each)
            else:
                # Calculate the distance between the new position and the hunter
                start_node = Node((each[0], each[1]))
                path = start_node.astar(game_map, hunter_node)
                distances.append(len(path))
        # Remove the invalid moves from the possible move list
        for each in trash_moves:
            possible_moves.remove(each)
        if len(distances) == 0 or current_distance > max(distances):
            return # Current position is already the best
        # Remove the moves that moves the prey closer to the hunter
        trash_moves = []
        for i, each in enumerate(distances):
            if each < max(distances):
                trash_distances.append(each)
                trash_moves.append(possible_moves[i])
        for each in trash_distances:
            distances.remove(each)
        for each in trash_moves:
            possible_moves.remove(each)
        # Choose the best move randomly if multiple moves result in the same distance
        best_move = possible_moves[randint(0, len(possible_moves)-1)]
        game_map.update(self.x, self.y, best_move[0], best_move[1], P)
        self.set_coordinate(best_move)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        game = Game()
        if  game.homepage() == 1:
            game.rules()
        else:
            difficulty = game.ask_difficulty()

            game_map = GameMap(10)

            h_coordinate, p_coordinate = game_map.setup_map(difficulty)
            hunter = Hunter(h_coordinate)
            prey = Prey(p_coordinate)

            game_map.print_game_state(hunter, game.moves)

            while not game.game_over:
                new_move = game.ask_move()
                new_x, new_y = hunter.x, hunter.y
                updated = True
                
                if (new_move == 'W' 
                    and hunter.y - hunter.speed > 0 and hunter.y - hunter.speed < game_map.size 
                    and not game_map.is_mountain(hunter.x, hunter.y - hunter.speed)):
                    new_y = hunter.y - hunter.speed
                elif (new_move == 'A' 
                    and hunter.x - hunter.speed > 0 and hunter.x - hunter.speed < game_map.size
                    and not game_map.is_mountain(hunter.x - hunter.speed, hunter.y)):
                    new_x = hunter.x - hunter.speed
                elif (new_move == 'S' 
                    and hunter.y + hunter.speed > 0 and hunter.y + hunter.speed < game_map.size 
                    and not game_map.is_mountain(hunter.x, hunter.y + hunter.speed)):
                    new_y = hunter.y + hunter.speed
                elif (new_move == 'D' 
                    and hunter.x + hunter.speed > 0 and hunter.x + hunter.speed < game_map.size
                    and not game_map.is_mountain(hunter.x+hunter.speed, hunter.y)):
                    new_x = hunter.x + hunter.speed
                elif new_move == 'E':
                    if not hunter.toggle():
                        print(coloured("Out of charges!", "red", attrs=["bold"]))
                else:
                    cprint("Cannot get up the mountain!", "red")
                    updated = False

                if new_x != hunter.x or new_y != hunter.y:
                    game_map.update(hunter.x, hunter.y, new_x, new_y, H)
                    hunter.set_coordinate((new_x, new_y))
                    if hunter.speed == 2:
                        hunter.charges -= 1
                    
                    if hunter.x == prey.x and hunter.y == prey.y:  # This means that the hunter has caught the prey
                        if not game.end():
                            raise SystemExit
                        updated = False

                if not game.game_over and  updated:
                    if hunter.charges == 0:
                        hunter.speed = 1
                    prey.make_move(game_map, (hunter.x, hunter.y))
                    if hunter.x == prey.x and hunter.y == prey.y:
                        if not game.end():
                            raise SystemExit
                    game_map.print_game_state(hunter, game.moves)


if __name__ == "__main__":
    main()