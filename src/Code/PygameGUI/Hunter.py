from Animal import Animal


class Hunter(Animal):
    """
    A class representing a hunter.
    """
    def __init__(self, coordinate: tuple, special_ability: int, fog: bool) -> None:
        """
        Initialize a new Hunter instance.

        :param coordinate:      The coordinate of the hunter.
        :param special_ability: The special ability of the hunter.
        :param fog:             Whether the fog is on or not.
        """
        super().__init__(coordinate[0], coordinate[1])
        abilities = ["Jumper", "Time Stopper", "Teleporter", "Spotter", "Baiter", "Shooter"]
        self.special_ability = abilities[special_ability - 1]
        self.special_status = False
        self.fog = fog
        self.visibility = 2 if fog else 100
        # Set the charges for different special abilities
        if self.special_ability == "Jumper":
            self.charges = 10
        elif self.special_ability == "Time Stopper":
            self.charges = 5
        elif self.special_ability == "Teleporter":
            self.charges = 1
        elif self.special_ability == "Baiter":
            self.charges = 3
        elif self.special_ability == "Spotter":
            self.charges = 3
        elif self.special_ability == "Shooter":
            self.charges = 1
        
    def reset_settings(self) -> None:
        """
        Set the default settings of the hunter.
        """
        self.speed = 1
        self.moves_on_turn = 1
        self.visibility = 2 if self.fog else 100
        self.special_status = False