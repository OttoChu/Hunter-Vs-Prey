from random import randint
from time import sleep
from termcolor import cprint, colored as coloured
import os

from Tiles import *

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

        :param difficulty:  A number between 1(easiest) - 6(hardest) representing the chosen difficulty.

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
        number_of_mountains = int(self.size * (6 - difficulty)*2)
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
    
    def is_map_reachable(self) -> bool:
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
    
    def depth_first_search(self, node: tuple, graph: dict, visited: set) -> set:
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

    def print_game_map(self, hunter_position: tuple, fog: bool, ability_name: str, ability_status: bool) -> None:
        """
        Print the map to the screen.

        :param hunter_position: The position of the Hunter.
        :param fog:             Whether the fog of war is enabled or not.
        :param ability_name:    The name of the Hunter's ability.
        :param ability_status:  Whether the Hunter is currently using their ability or not.
        """
        # Print the whole map to the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        if not fog:
            for each_row in self.game_map:
                line = ""
                for each_item in each_row:
                    line += each_item 
                print(line)
        else:
            visibility = 5 if ability_status and ability_name == "Spotter" else 2
            hunter_x, hunter_y = hunter_position
            for y in range(self.size):
                line = ""
                for x in range(self.size):
                    if abs(x - hunter_x) <= visibility and abs(y - hunter_y) <= visibility:
                        line += self.game_map[y][x]
                    else:
                        line += F + ' '
                print(line)
        print()

    def print_state_description(self, special: bool, charges_left: int,
            moves: int, moves_left: int, ability_name: str, charge_error: bool = False, 
            mountain_error: bool= False, input_error: bool = False) -> None:
        """
        Print the state description to the screen.

        :param special:         Whether the Hunter is currently using a special ability.
        :param charges_left:    The number of charges left.
        :param moves:           The number of moves the Hunter has made.
        :param moves_left:      The number of moves the Hunter has left on the current turn.
        :param ability_name:    The name of the Hunter's ability.
        :param charge_error:    Whether the Hunter tried to use a charge when they had none left.
        :param mountain_error:  Whether the Hunter tried to move into a mountain.
        :param input_error:     Whether the Hunter entered an invalid input.
        """
        print("Your special ability is " + coloured(f"{ability_name}", "yellow") + "!")
        print("You have " + coloured(str(charges_left), "red", attrs=["bold"]) + " charge(s) left!")
        if special:
            print("You " + coloured("are", "red", attrs=["bold"]) + " currently using a charge.")
        print("You have " + coloured(str(moves_left), "green") + " move(s) left on this turn!")
        print()
        print("This is your " + coloured(f"{moves}th ", "green") + "move.")
        print()
        # Print the error messages
        if charge_error:
            cprint("Out of charges!", "red", attrs=["bold"])
        if mountain_error:
            cprint("Cannot move into a mountain!", "red", attrs=["bold"])
        if input_error:
            cprint("Invalid input!", "red", attrs=["bold"])

    def is_mountain(self, x: int, y: int) -> bool:
        """
        Check if the target square is a mountain.

        :param x:   The x coordinate of the target square.
        :param y:   The y coordinate of the target square.

        :return:    A boolean representing whether the target square is a mountain or not.
        """
        return self.game_map[y][x] == M

    def update(self, old_x: int, old_y: int, new_x: int, new_y: int, target: str) -> None:
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