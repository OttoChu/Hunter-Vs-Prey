from Animals.Animal import Animal


class Hunter(Animal):
    """
    A class representing a hunter.
    """
    def __init__(self, coordinate: tuple, special_ability: int) -> None:
        """
        Initialize a new Hunter instance.

        :param coordinate:      The coordinate of the hunter.
        :param special_ability: The special ability of the hunter.
        """
        super().__init__(coordinate[0], coordinate[1])
        abilities = ["Jumper", "Time Stopper", "Teleporter", "Baiter", "Spotter", "Shooter"]
        self.special_ability = abilities[special_ability - 1]
        self.special_status = False
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
        
    def default_settings(self) -> None:
        """
        Set the default settings of the hunter.
        """
        self.speed = 1
        self.moves_on_turn = 1
        self.charges = 0
        self.special_status = False

    def toggle_special_move(self) -> bool:
        """
        Toggle the special power of the hunter. Also changes the corresponding settings of the hunter.

        :return:    True if the special power is toggled on, False otherwise.
        """
        if self.charges == 0: # The hunter has no charges left
            self.default_settings()
            return False
        
        self.special_status = not self.special_status # Toggle the special status
        
        if self.special_ability == "Jumper":
            # make the hunter move 2 tiles instead of 1 on the next turn
            if self.speed == 1:
                self.speed = 2
            else:
                self.speed = 1
        
        elif self.special_ability == "Time Stopper":
            # make the hunter make 3 moves in one turn
            if self.moves_on_turn == 1:
                self.moves_on_turn = 3
            else:
                self.moves_on_turn = 1

        elif self.special_ability == "Teleporter":
            # teleport the hunter to a random location on the map
            pass
        
        elif self.special_ability == "Baiter":
            raise NotImplementedError
        
        elif self.special_ability == "Spotter":
            # show 10x10 area instead of 5x5 in fog of war
            # TODO: implement this
            pass

        
        elif self.special_ability == "Shooter":
            raise NotImplementedError
        
        return True