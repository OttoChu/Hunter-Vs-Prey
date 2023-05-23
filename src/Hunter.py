from Animal import Animal


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