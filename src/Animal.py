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