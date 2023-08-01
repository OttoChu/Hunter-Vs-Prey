from random import randint

from Tiles import *

class Game():
    '''
    This class is used to store the game data and logic.
    '''
    def __init__(self) -> None:
        '''
        This function initializes the class.
        '''
        self.game_over = False # Whether the game is over
        self.fog_of_war = False # Whether the fog of war is enabled
        self.all_difficulties = ["EXTRA EASY", "EASY", "NORMAL", "HARD", "EXTRA HARD", "IMPOSSIBLE"] # A list of all the difficulties.
        self.all_abilities = ["JUMPER", "TIME STOPPER", "TELEPORTER", "SPOTTER", "BAITER", "SHOOTER"] # A list of all the abilities.
        self.chosen_difficulty = 3 # The difficulty chosen by the player
        self.chosen_ability = 1 # The ability chosen by the player
        self.moves = 1 # The number of moves the player has made

        self.board_size = 15 # The size of the board
        self.board = [] # The board of the game

    def setup_board(self, difficulty: int) -> None:
        """
        Generates a new board with the Hunter and Prey depending on the difficulty chosen.

        :param difficulty:  A number between 1(easiest) - 6(hardest) representing the chosen difficulty.
        """
        if difficulty == 1: # Extra Easy
            self.board = [[M for _ in range(self.board_size)] for _ in range(self.board_size)]
            self.board[1][1] = H
            self.board[1][2] = P
            return
        
        # Fill the border of the board with mountains
        self.board = [[M for _ in range(self.board_size)] if i == 0 or i == self.board_size - 1 else [
            M if i == 0 or i == self.board_size - 1 else T for i in range(self.board_size)] 
            for i in range(self.board_size)]
            
        # Add mountains to the board randomly based on the difficulty chosen
        number_of_mountains = int(self.board_size * (6 - difficulty)*2)
        for _ in range(number_of_mountains):
            while (True):
                x = randint(1, self.board_size - 1)
                y = randint(1, self.board_size - 1)
                if self.board[y][x] != M:
                    self.board[y][x] = M
                    if self.is_board_reachable():
                        break
                    else:
                        self.board[y][x] = T
        # Add the Hunter onto the board
        while True:
            hunter_x = randint(1, self.board_size - 1)
            hunter_y = randint(1, self.board_size - 1)
            if self.board[hunter_y][hunter_x] != M:
                self.board[hunter_y][hunter_x] = H
                break # Break out of the loop once the Hunter has been added to the board

        # Add the Prey onto the board        
        while True:
            # TODO: Add a loading screen?
            #       The loading screen could be a progress bar that fills up as the board is being generated?

            prey_x = randint(1, self.board_size - 1)
            prey_y = randint(1, self.board_size - 1)
            if self.board[prey_y][prey_x] != M and (prey_x, prey_y) != (hunter_x, hunter_y):
                self.board[prey_y][prey_x] = P
                break # Break out of the loop once the Prey has been added to the board

    def setup_game(self, difficulty: int, ability: int) -> None:
        """
        Sets up the game.

        :param difficulty:  A number between 1(easiest) - 6(hardest) representing the chosen difficulty.
        :param ability:     A number between 1 and 3 representing the chosen ability.
        """
        self.setup_board(difficulty)
        self.chosen_difficulty = difficulty
        self.chosen_ability = ability
        self.moves = 1
        self.game_over = False
    
    def is_board_reachable(self) -> bool:
        """
        Check if the board is reachable.

        :return: True if the board is reachable, False otherwise.
        """
        # Convert 2D array to graph
        graph = {}
        rows, cols = len(self.board), len(self.board[0])
        for i in range(rows):
            for j in range(cols):
                if self.board[i][j] != M:
                    neighbors = []
                    if i > 0 and self.board[i-1][j] != M:
                        neighbors.append((i-1, j))
                    if i < rows-1 and self.board[i+1][j] != M:
                        neighbors.append((i+1, j))
                    if j > 0 and self.board[i][j-1] != M:
                        neighbors.append((i, j-1))
                    if j < cols-1 and self.board[i][j+1] != M:
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

    def is_mountain(self, position: tuple) -> bool:
        """
        Check if the target square is a mountain.

        :param position:    The position of the target square.

        :return:    A boolean representing whether the target square is a mountain or not.
        """
        return self.board[position[1]][position[0]] == M

    def update_board(self, old_position: tuple, new_position: tuple, animal_type: str) -> None:
        """
        Update the board with the new position of the Hunter.

        :param old_position:    The old position of the Animal.
        :param new_position:    The new position of the Animal.
        :param animal_type:     The type of Animal.
        """
        self.board[new_position[1]][new_position[0]] = animal_type
        self.board[old_position[1]][old_position[0]] = T
        
    def get_animal_position(self) -> tuple:
        """
        Get the position of the Hunter and Prey.

        :return:    A tuple containing the position of the Hunter and Prey.
        """
        hunter_position = ()
        prey_position = ()
        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.board[y][x] == H:
                    hunter_position = (x, y)
                elif self.board[y][x] == P:
                    prey_position = (x, y)
                if hunter_position != () and prey_position != ():
                    return hunter_position, prey_position       