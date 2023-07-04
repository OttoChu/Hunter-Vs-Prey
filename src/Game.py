import msvcrt
import os
from termcolor import cprint, colored as coloured

from Tiles import *

class Game:
    """
    The main class that runs the game.
    """
    def __init__(self) -> None:
        """
        Initialize the game.
        """
        self.moves = 0 # The number of moves the player has made.
        self.game_over = False # A boolean that indicates whether the game is over or not.
        self.fog_of_war = False # A boolean that indicates whether the fog of war is on or not.
        self.all_difficulties = ["EXTRA EASY", "EASY", "NORMAL", "HARD", "EXTRA HARD", "IMPOSSIBLE"] # A list of all the difficulties.
        self.all_abilities = ["JUMPER", "TIME STOPPER", "TELEPORTER", "SPOTTER", "BAITER", "SHOOTER"] # A list of all the abilities.
        self.chosen_difficulty = 3 # A number representing the chosen difficulty. Default is 3.
        self.chosen_ability = 1 # A number representing the chosen ability. Default is 1.
    
    def homepage(self) -> int:
        """
        Print the homepage onto the screen. Ask for input for what to show next.

        :return: The option chosen by the user.
        """
        cprint("Welcome to Hunter Vs Prey!", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "magenta") + coloured("New Game", "yellow"))
        print(coloured("2. ", "magenta") + coloured("Rules", "yellow"))
        print(coloured("3. ", "magenta") + coloured("Settings", "yellow"))
        print(coloured("4. ", "magenta") + coloured("Quit", "yellow"))
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return option
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def rules(self) -> None:
        """
        Print all the rules onto the screen.
        """
        cprint("Rules", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "magenta") + coloured("The Prey is represented as 🦊.", "yellow"))
        print(coloured("2. ", "magenta") + coloured("The Hunter is represented as 👨.", "yellow"))
        print(coloured("3. ", "magenta") + coloured("All animals can move 1 tile in any direction per turn. (excluding diagonals)", "yellow"))
        print(coloured("4. ", "magenta") + coloured("The squares that you can be on are represented as 🌳.", "yellow"))
        print(coloured("5. ", "magenta") + coloured("The squares that you can NOT be on are represented as 🗻.", "yellow"))
        print(coloured("6. ", "magenta") + coloured("Invalid move will increment your total moves by 1!", "yellow"))
        print(coloured("7. ", "magenta") + coloured("Toggling your special move will count as a turn.", "yellow"))
        print()
        print("Here are the accepted inputs:")
        print(coloured("W ", "blue") + coloured("to move up.", "yellow"))
        print(coloured("A ", "blue") + coloured("to move left.", "yellow"))
        print(coloured("S ", "blue") + coloured("to move down.", "yellow"))
        print(coloured("D ", "blue") + coloured("to move right.", "yellow"))
        print(coloured("E ", "blue") + coloured("to toggle special move on or off.", "yellow"))
        cprint("Any other input will be considered invalid!", "red", attrs=["bold"])
        print()
        print("Goal:")
        cprint("Catch the Prey in the least number of moves!", "yellow")
        cprint("The Prey will try to escape from you!", "yellow")
        print()
        print("Good luck!")
        self.print_press_to_continue()

    def settings(self) -> int:
        """
        Print all the settings onto the screen.

        :return:    An integer representing the option chosen. 1 for difficulty, 2 for fog of war, 3 for special abilities, 4 for back.
        """
        cprint("Settings", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "magenta") + coloured("Difficulty", "yellow"))
        print(coloured("2. ", "magenta") + coloured("Fog of War", "yellow"))
        print(coloured("3. ", "magenta") + coloured("Special Ability", "yellow"))
        print(coloured("4. ", "magenta") + coloured("Back", "yellow"))
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return option
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def choose_difficulty(self) -> int:
        """
        Print the difficulty screen onto the screen. Ask for input for what difficulty to choose.

        :return:    An integer representing the difficulty chosen. 1 for extra easy, 2 for easy, 3 for normal, 4 for hard, 5 for extra hard, 6 for impossible, 7 for back.
        """
        cprint("Difficulty", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "magenta") + coloured("Extra Easy", "yellow"))
        print(coloured("2. ", "magenta") + coloured("Easy", "yellow"))
        print(coloured("3. ", "magenta") + coloured("Normal", "yellow"))
        print(coloured("4. ", "magenta") + coloured("Hard", "yellow"))
        print(coloured("5. ", "magenta") + coloured("Extra Hard", "yellow"))
        print(coloured("6. ", "magenta") + coloured("Impossible", "yellow"))
        print(coloured("7. ", "magenta") + coloured("Back", "yellow"))
        print()
        cprint(f"Current difficulty: {self.all_difficulties[self.chosen_difficulty - 1]}", "blue")
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 7:
                    if option < 7:
                        self.chosen_difficulty = option
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return option
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def choose_fog_of_war(self) -> int:
        """
        Print the fog of war screen onto the screen. Ask for input for whether to turn on the fog of war.

        :return:    An integer representing the option chosen. 1 for yes, 2 for no, 3 for back.
        """
        cprint("Fog of War", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "magenta") + coloured("On", "yellow"))
        print(coloured("2. ", "magenta") + coloured("Off", "yellow"))
        print(coloured("3. ", "magenta") + coloured("Back", "yellow"))
        print()
        print("Note:")
        print("The Spotter ability is " + coloured("UNAVAILABLE", "red") + " if Fog of War is off.")
        print("The " + coloured("Jumper", "yellow") + " ability will be chosen instead.")
        print()
        cprint(f"Current fog of war: {'ON' if self.fog_of_war else 'OFF'}", "blue")
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 3:
                    if option < 3:
                        if self.chosen_ability == 4 and option == 2:
                            self.chosen_ability = 1
                        self.fog_of_war = True if option == 1 else False
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return option
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def choose_special_ability(self) -> int:
        """
        Print the special ability screen onto the screen. Ask for input for special ability to use.

        :return:    An integer representing the option chosen. 1 for Jumper, 2 for Time Stopper, 3 for back.
        """
        cprint("Special Ability", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "magenta") + coloured("Jumper", "yellow"))
        print("\t Moves 2 tiles in the same direction in one turn.")
        print("\t This includes moving over mountains.")
        print("\t You can only use this ability " + coloured("10 ", "red") + "times per game.")
        print(coloured("2. ", "magenta") + coloured("Time Stopper", "yellow"))
        print("\t Makes 3 moves in the same turn.")
        print("\t During this time, the Prey will not move.")
        print("\t You can only use this ability " + coloured("5 ", "red") + "times per game.")
        print(coloured("3. ", "magenta") + coloured("Teleporter", "yellow"))
        print("\t Teleports to a tile on the map.")
        print("\t This is only the 9x9 area around the Hunter.")
        print(f"\t You can only teleport to a {T} tile.")
        print("\t You can end this ability early.")
        print("\t You can only use this ability " + coloured("once ", "red") + "per game.")
        print(coloured("4. ", "magenta") + coloured("Spotter", "yellow"))
        print("\t Reveals 11x11 area around the Hunter.")
        print("\t Choosing his ability will turn Fog of War " + coloured("ON.", "red"))
        print("\t You can only use this ability " + coloured("3 ", "red") + "times per game.")
        print(coloured("5. ", "magenta") + coloured("Back", "yellow"))
        print()
        cprint(f"Current chosen special ability: {self.all_abilities[self.chosen_ability - 1]}", "blue")
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 5:     
                    if option < 5:
                        if option == 4:
                            self.fog_of_war = True
                        self.chosen_ability = option
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return option
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def end(self) -> bool:
        """
        Print the end screen onto the screen. Ask for input for whether to play again.

        :return: A boolean that indicates whether the player wants to play again.
        """
        self.game_over = True
        os.system('cls' if os.name == 'nt' else 'clear')
        cprint("The hunter has eaten the prey!", "green", "on_red")
        cprint(" __     ______  _    _  __          _______ _   _   _ \n \ \   / / __ \| |  | | \ \        / /_   _| \ | | | |\n  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | | |\n   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | | |\n    | | | |__| | |__| |    \  /\  /   _| |_| |\  | |_|\n    |_|  \____/ \____/      \/  \/   |_____|_| \_| (_)\n", "red")
        print(f"You caught the prey in {self.moves} moves.")
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
            cprint("Invalid input!", "red")
            
    def find_teleport_map(self, game_map: list, hunter_position: tuple) -> list:
        """
        Find the teleport map for the Teleporter ability.

        :param game_map:        The game map.
        :param hunter_position: The position of the Hunter.

        :return:                A list of strings representing the teleport map.
        """
        valid_locations = []
        hunter_x, hunter_y = hunter_position
        # Get the 8x8 area around the Hunter.
        for y in range(hunter_y - 4, hunter_y + 5):
            line = ""
            if 0 < y < len(game_map):
                for x in range(hunter_x - 4, hunter_x + 5):
                    if 0 < x < len(game_map):
                        line += game_map[y][x]
                    else:
                        line += M
            else:
                line = M * 9
            valid_locations.append(line)
        return valid_locations
    
    def print_press_to_continue(self) -> None:
        """
        Print the press to continue screen onto the screen.
        """
        print()
        cprint("Press any key to continue...", "magenta")
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_teleport_location(self, teleport_map: list, chosen_x: int = 0, chosen_y: int = 0) -> None:
        """
        Print the valid teleport locations onto the screen and show the rules for teleporting.
        It will also highlight the chosen row, column and square (if chosen).

        :param teleport_map:    A list of strings that represents the teleport map.
        :param chosen_x:        An integer that represents the chosen x coordinate.
        :param chosen_y:        An integer that represents the chosen y coordinate.
        """
        if chosen_x != 0 and chosen_y != 0: # show chosen square
            teleport_map[chosen_y - 1] = teleport_map[chosen_y - 1][:chosen_x - 1] + S + teleport_map[chosen_y - 1][chosen_x:]
        show_x = ""      
        if chosen_x != 0: # show the chosen column
            show_x = "    " + "  " * (chosen_x - 1) + Y
            print(show_x)
        else: 
            print()
        y_num = "     "
        for i in range(len(teleport_map)):
            y_num += str(i + 1) +' '
        print(y_num)
        for i, each in enumerate(teleport_map):
            if i == chosen_y - 1:
                print(Y + ' ' + str(i + 1) + each + Y)
            else:
                print("   " + str(i + 1) + each)
        print(show_x)
        print()
        if chosen_x == 0 or chosen_y == 0:
            print(f"You can only teleport to {T}")
            print(f"Canceling or teleporting to {M} or {P} or {F} " + coloured("WILL", "red") +  " still use up a charge.")
            print("Press " + coloured('Q', "green") + " to cancel.")
            print()
        
    def ask_move(self) -> str:
        """
        Ask the user for the next move.

        :return: A string that represents the next move.
        """
        while True:
            move = msvcrt.getch()
            try:
                move = move.decode("utf-8").upper()
                return move
            except UnicodeDecodeError:
                pass
            return

    def ask_teleport_location(self, game_map: list, hunter_position: tuple) -> tuple:
        """
        Allow the user to choose where to teleport to.
        Valid locations are any tile that is not a mountain or fog or the prey.
        The teleportation area is the 8x8 around surrounding the Hunter.

        :param game_map:        The game map.
        :param hunter_position: The position of the Hunter.

        :return: A tuple representing the new position of the Hunter.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        valid_locations = self.find_teleport_map(game_map, hunter_position)
        self.print_teleport_location(valid_locations)
        print("Choose the column number to teleport to:")
        while True:
            x_pos = msvcrt.getch()
            try:
                x_pos = x_pos.decode("utf-8").upper()
                if x_pos == "Q": # Cancel
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return hunter_position, False
                elif int(x_pos) > 0 and int(x_pos) <= len(valid_locations):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_teleport_location(valid_locations, int(x_pos))
                    print("You have chosen the " + coloured(f"{x_pos}th", "yellow") + " column.")
                    print()
                    print("Choose the row number to teleport to:")
                    while True:
                        y_pos = msvcrt.getch()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        try:
                            y_pos = y_pos.decode("utf-8").upper()
                            if y_pos == "Q": # Cancel
                                return hunter_position, False
                            elif int(y_pos) > 0 and int(y_pos) <= len(valid_locations):
                                if valid_locations[int(y_pos) - 1][int(x_pos) - 1] != T : # invalid location
                                    print("Unable to teleport to your chosen location.")
                                    print("You will " + coloured("not", "red") + " be teleported but a charge will still be used.")
                                    self.print_press_to_continue()
                                    return hunter_position, False
                                else: # valid location
                                    self.print_teleport_location(valid_locations, int(x_pos), int(y_pos))
                                    print("You have chosen the " + coloured(f"{y_pos}th", "yellow") + " row.")
                                    print(f"You will teleport to the square marked by a {S}.")
                                    self.print_press_to_continue()
                                    return (hunter_position[0] - 5 + int(x_pos), hunter_position[1] - 5 + int(y_pos)), True
                        except (UnicodeDecodeError, ValueError):
                            pass
                        cprint("Invalid input!", "red")
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def reset(self) -> None:
        """
        Reset the game state.
        """
        self.game_over = False
        self.moves = 0        