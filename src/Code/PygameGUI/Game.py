class Game():
    '''
    This class is used to store the game data and logic.
    '''
    def __init__(self) -> None:
        '''
        This function initializes the class.
        '''
        self.game_over = False # Whether the game is over
        self.moves = 0 # The number of moves the player has made
        self.fog_of_war = False # Whether the fog of war is enabled
        self.chosen_difficulty = 3 # The difficulty chosen by the player
        self.chosen_ability = 1 # The ability chosen by the player

        self.board = [] # The board of the game
        