# Hunter Vs Prey v1.4.0

from random import randint, choice
from time import sleep
import os
from termcolor import cprint, colored as coloured
import msvcrt

from AStarPathFinding import a_star_pathfinding
from FurthestPosition import furthest_position

T = Tree = "🌳"
P = Prey = "🦊"
H = Hunter = "👨"
M = Mountain = "🗻"


class Game:
    def __init__(self):
        self.game_over = False
        self.moves = 0
    
    def homepage(self) -> int:
        """
        Print the homepage onto the screen.
        Ask for input for what to show next.

        :returns mode:  The mode chosen to show next. (1 for rules, 2 for new game)
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
        Print all the accepted input onto the screen.
        """
        print('Here are the accepted inputs:')
        cprint("'W' to move upwards", 'red')
        cprint("'A' to move to the left", 'blue')
        cprint("'S' to move downwards", 'yellow')
        cprint("'D' to move to the right", 'magenta')
        print()
        cprint("'E' to toggle the special move", "green")
        print()
        print("Rules")
        print("1. If an invalid move is made, " + coloured("your total move will be incremented by 1!", "red"))
        print("2. You starts with 10 special moves.")
        print("3. Toggling your special move will count as a turn.")
        print()
        cprint("Press anything to return to the homepage.", "black")
        _ = msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')

    def end(self) -> bool:
        """
        Show the player that they have completed the game and ask if they wanted to play agin.

        :returns: A boolean that indicates whether the player wants to play again or not.
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
        Ask the user to choose the game difficult.

        :returns difficulty:    A number between 1(easiest) - 5(hardest) representing the chosen difficulty.
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
        Ask the user for a new move. 
        Will keep asking unless unless "WASD" or "E" (special move key) is entered.
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
        self.size = size

    def setup_map(self, difficulty: int) -> tuple:
        """
        Generates a new map with the Hunter and Prey

        :returns:    A tuple (hunter coordinates, prey coordinates) with each coordinate containing the corresponding x and y coordinate.
        """
        # Make the very easy difficulty map 
        if difficulty == 1:
            self.game_map = [[M for _ in range(self.size)] for _ in range(self.size)]
            self.game_map[1][1] = H
            self.game_map[1][2] = P
            return ((1,1), (2,1))
        # Fill get the border of the map with mountains
        self.game_map = [[M for _ in range(self.size)] if i == 0 or i == self.size - 1 else [
            M if i == 0 or i == self.size - 1 else T for i in range(self.size)] 
            for i in range(self.size)]
        # Add mountains to the map randomly based on the difficulty chosen
        number_of_mountains = self.size * (6 - difficulty)
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
        while True:  # Add the Prey onto the map
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
        Determines if all parts of a game map are reachable from some starting position.

        :returns: A boolean showing wether all parts of the map is reachable
        """
        # convert 2D array to graph
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
        
        # traverse graph to check reachability
        visited = set()
        start_node = next(iter(graph))  # choose an arbitrary node as starting point
        self.depth_first_search(start_node, graph, visited)
        return len(visited) == len(graph)
    
    def depth_first_search(self, node: tuple, graph: dict, visited: set):
        """
        Traverses a graph depth-first, starting from the given node, and marks all visited nodes.
        
        :param node:    A tuple representing the starting node.
        :param graph:   A dictionary that maps each node to a list of its neighboring nodes.
        :param visited: A set of nodes that have already been visited.
        """
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.depth_first_search(neighbor, graph, visited)

    def print_game_state(self, hunter:Hunter):
        """
        Print the whole map with the charges left to the screen.

        :param hunter:  The current Hunter instance.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
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

    def is_mountain(self, x: int, y: int) -> bool:
        """
        Checks whether the target square is a mountain or not.

        :param x:   The x coordinate of the target square.
        :param y:   The y coordinate of the target square.

        :returns:   A boolean representing whether the target square is a mountain or not.
        """
        return self.game_map[y][x] == M

    def update(self, old_x: int, old_y: int, new_x: int, new_y: int, target: str):
        """
        Update the game map with the new move.

        :param old_x:   The x coordinate of old the target square.
        :param old_y:   The y coordinate of old the target square.
        :param new_x:   The x coordinate of new the target square.
        :param new_y:   The y coordinate of new the target square.
        """
        self.game_map[new_y][new_x] = target
        self.game_map[old_y][old_x] = T


class Animal():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.speed = 1


class Hunter(Animal):
    def __init__(self, coordinate: tuple):
        self.charges = 10 
        super().__init__(coordinate[0], coordinate[1])

    def set_coordinate(self, coordinate: tuple):
        """
        Updates the coordinates for the hunter.

        :param coordinate: The new coordinate for the hunter.
        """
        self.x = coordinate[0]
        self.y = coordinate[1]

    def toggle(self) -> bool:
        """
        Toggles between the special move state.
        It will only activate the special move if charge is larger than 0.

        :returns:   A boolean that indicates whether the toggle was successful or not.
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
    def __init__(self, coordinate: tuple):
        self.breathing = True
        super().__init__(coordinate[0], coordinate[1])

    def set_coordinate(self, coordinate: tuple):
        """
        Store a new coordinate for the prey.

        :param coordinate:  The new coordinate for the prey.
        """
        self.x = coordinate[0]
        self.y = coordinate[1]

    def make_move(self, game_map: GameMap, hunter_pos:tuple) -> None:
        """
        The Prey makes a move based on something. If the prey tries to go onto a square with either 
        a mountain or the hunter, it will miss its chance to move.

        :param game_map:    The current game map.
        :param hunter_pos:  The position of the hunter.

        :returns:           None if the prey is already at the furthest point away from the hunter or 
                            there is no path to the furthest point
        TODO it finds the furthest spot but may still go towards the hunter
        """

        furthest = furthest_position(game_map.game_map, hunter_pos, (self.x, self.y))
        if furthest == (self.x, self.y):
            return None
        path = a_star_pathfinding(game_map.game_map, (self.x, self.y), furthest)
        if path == None:
            return None
        next_coordinate = path[1]
        if game_map.game_map[next_coordinate[1]][next_coordinate[0]] == M:
            return None
        game_map.update(self.x, self.y, next_coordinate[0], next_coordinate[1], P)
        self.set_coordinate(next_coordinate)


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

            game_map.print_game_state(hunter)

            while not game.game_over:
                new_move = game.ask_move()
                new_x, new_y = hunter.x, hunter.y
                
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
                        updated = True

                if not game.game_over and not updated:
                    if hunter.charges == 0:
                        hunter.speed = 1
                    prey.make_move(game_map, (hunter.x, hunter.y))
                    if hunter.x == prey.x and hunter.y == prey.y:
                        if not game.end():
                            raise SystemExit
                    game_map.print_game_state(hunter)



if __name__ == "__main__":
    main()