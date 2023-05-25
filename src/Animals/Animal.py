class Animal():
    """
    A class representing an animal.
    """
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a new Animal instance.
        
        :param x:   The x coordinate of the animal.
        :param y:   The y coordinate of the animal.
        """
        self.x = x
        self.y = y
        self.speed = 1 # The speed of the animal
        self.moves_on_turn = 1 # The amount of moves the animal can make on a turn

    def set_coordinate(self, coordinate: tuple) -> None:
        """
        Store a new coordinate for the animal.

        :param coordinate:  The new coordinate for the animal.
        """
        self.x = coordinate[0]
        self.y = coordinate[1]