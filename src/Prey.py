from random import randint

from Animal import Animal
from GameMap import *
from Node import Node
from Tiles import *

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