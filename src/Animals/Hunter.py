from Animals.Animal import Animal


class Hunter(Animal):
    """
    A class representing a hunter.
    """
    # TODO: Add a special power attribute to the hunter. This is just temporary!
    def __init__(self, coordinate: tuple, special_ability: str = "Time Stopper"):
        """
        Initialize a new Hunter instance.

        :param coordinate:  The coordinate of the hunter.
        """
        super().__init__(coordinate[0], coordinate[1])
        self.special_status = False
        self.special_ability = special_ability
        if self.special_ability == "Jumper":
            self.charges = 10
        elif self.special_ability == "Time Stopper":
            self.charges = 5
        elif self.special_ability == "Teleporter":
            self.charges = 1
        elif self.special_ability == "Baiter":
            self.charges = 3
        elif self.special_ability == "Spotter":
            self.charges = 2
        

    def default_settings(self) -> None:
        """
        Set the default settings of the hunter.
        """
        # TODO: Change all the default settings to the default settings of the hunter
        self.speed = 1
        self.moves_on_turn = 1
        self.charges = 0
        self.special_status = False
        
    def toggle_special_move(self) -> bool:
        """
        Toggle the special power of the hunter.

        :return:    True if the special power is toggled on, False otherwise.
        """
        if self.charges == 0: # The hunter has no charges left
            self.default_settings()
            return False
        
        if self.special_ability == "Jumper":
            if self.speed == 1:
                self.special_status = True
                self.speed = 2
            else:
                self.special_status = False
                self.speed = 1
            return True
        
        elif self.special_ability == "Time Stopper":
            # TODO: Implement the speedy boi special power
            # it should be able to make 2 moves in one turn
            if self.moves_on_turn == 1:
                self.special_status = True
                self.moves_on_turn = 3
            else:
                self.special_status = False
                self.moves_on_turn = 1
            return True
        
        elif self.special_ability == "Teleporter":
            # TODO: Implement the teleporter special power
            # it should be able to teleport to any tile on the map (except the wall)
            pass

        elif self.special_ability == "Baiter":
            # TODO: Implement the baiter special power
            # it should be able to place a bait in a 5x5 area next to the Hunter on the map (except the wall)
            # the bait should be able to attract the prey to it 
            # (only if the prey is close enough (distance to do set later))
            pass

        elif self.special_ability == "Spotter":
            # TODO: Implement the spotter special power
            # This should only be useable in fog of war mode
            # it should be able to reveal a 10x10 area around the hunter instead of the normal 5x5
            pass

        elif self.special_ability == "Shooter":
            # TODO: Implement the shooter special power
            # it should be able to shoot a bullet in a straight line in any direction
            # the bullet should be able to kill the prey if it hits it
            pass