import msvcrt
import os
from termcolor import cprint, colored as coloured

class Game:
    """
    The main class that runs the game.
    """
    def __init__(self) -> None:
        """
        Initialize the game.
        """
        self.game_over = False # A boolean that indicates whether the game is over or not.
        self.moves = 0 # The number of moves the player has made.
        self.difficulty = 3 # A number between 1(easiest) - 6(hardest) representing the chosen difficulty. Default is 3.
        self.abilities = 1 # A number representing the chosen abilities. Default is 1.
        self.fog_of_war = False # A boolean that indicates whether the fog of war is on or not.
    
    def homepage(self) -> int:
        """
        Print the homepage onto the screen. Ask for input for what to show next.

        :return: The option chosen by the user.
        """
        cprint("Welcome to Hunter Vs Prey!", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "black") + coloured("New Game", "yellow"))
        print(coloured("2. ", "black") + coloured("Rules", "yellow"))
        print(coloured("3. ", "black") + coloured("Settings", "yellow"))
        print(coloured("4. ", "black") + coloured("Quit", "yellow"))
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
        print(coloured("1. ", "black") + coloured("The Prey is represented as 🦊.", "yellow"))
        print(coloured("2. ", "black") + coloured("The Hunter is represented as 👨.", "yellow"))
        print(coloured("3. ", "black") + coloured("Both the Hunter and Prey can move 1 square at a time.", "yellow"))
        print(coloured("4. ", "black") + coloured("The squares that you can be on are represented as 🌳.", "yellow"))
        print(coloured("5. ", "black") + coloured("The squares that you can NOT be on are represented as 🗻.", "yellow"))
        print(coloured("6. ", "black") + coloured("Invalid move will increment your total moves by 1!", "yellow"))
        print(coloured("7. ", "black") + coloured("You start with 10 special ability charges.", "yellow"))
        print(coloured("8. ", "black") + coloured("Invalid move will remove 1 charge.", "yellow"))
        print(coloured("8. ", "black") + coloured("Toggling your special move will count as a turn.", "yellow"))
        print()
        print("Here are the accepted inputs:")
        print(coloured("W ", "blue") + coloured("to move up.", "yellow"))
        print(coloured("A ", "blue") + coloured("to move left.", "yellow"))
        print(coloured("S ", "blue") + coloured("to move down.", "yellow"))
        print(coloured("D ", "blue") + coloured("to move right.", "yellow"))
        print(coloured("E ", "blue") + coloured("to toggle special move on or off.", "yellow"))
        cprint("Any other input will be considered invalid!", "red", attrs=["bold"])
        print()
        print("The goal of the game is the catch the Prey in the least number of moves!")
        print()
        cprint("Press anything to return to the homepage.", "black")
        _ = msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')

    def settings(self) -> int:
        """
        Print all the settings onto the screen.

        :return:    An integer representing the option chosen. 1 for difficulty, 2 for fog of war, 3 for special abilities, 4 for back.
        """
        cprint("Settings", "green", attrs=["bold"])
        print()
        print(coloured("1. ", "black") + coloured("Difficulty", "yellow"))
        print(coloured("2. ", "black") + coloured("Fog of War", "yellow"))
        print(coloured("3. ", "black") + coloured("Special Ability", "yellow"))
        print(coloured("4. ", "black") + coloured("Back", "yellow"))
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
        print(coloured("1. ", "black") + coloured("Extra Easy", "yellow"))
        print(coloured("2. ", "black") + coloured("Easy", "yellow"))
        print(coloured("3. ", "black") + coloured("Normal", "yellow"))
        print(coloured("4. ", "black") + coloured("Hard", "yellow"))
        print(coloured("5. ", "black") + coloured("Extra Hard", "yellow"))
        print(coloured("6. ", "black") + coloured("Impossible", "yellow"))
        print(coloured("7. ", "black") + coloured("Back", "yellow"))
        print()
        difficulties = ["EXTRA EASY", "EASY", "NORMAL", "HARD", "EXTRA HARD", "IMPOSSIBLE"]
        cprint(f"Current difficulty: {difficulties[self.difficulty - 1]}", "blue")
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 7:
                    if option < 6:
                        self.difficulty = option
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
        print(coloured("1. ", "black") + coloured("On", "yellow"))
        print(coloured("2. ", "black") + coloured("Off", "yellow"))
        print(coloured("3. ", "black") + coloured("Back", "yellow"))
        print()
        cprint(f"Current fog of war: {'ON' if self.fog_of_war else 'OFF'}", "blue")
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 3:
                    if option < 3:
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
        print(coloured("1. ", "black") + coloured("Jumper", "yellow"))
        print("\t Allows you to move 2 tiles at once.")
        print("\t This includes moving over mountains.")
        print("\t You can only use this ability " + coloured("10 ", "red") + "times per game.")
        print(coloured("2. ", "black") + coloured("Time Stopper", "yellow"))
        print("\t Allows you to stop time for 3 turns.")
        print("\t During this time, the Prey will not move.")
        print("\t You can only use this ability " + coloured("5 ", "red") + "times per game.")
        print(coloured("3. ", "black") + coloured("Back", "yellow"))
        print()
        abilities = ["JUMPER", "TIME STOPPER"]
        cprint(f"Current chosen special ability: {abilities[self.abilities - 1]}", "blue")
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 3:
                    if option < 3:
                        self.special_abilities = option
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
            
    def ask_fog_of_war(self) -> bool:
        """
        Ask the user for the fog of war setting.
        
        :return: A boolean that indicates whether the fog of war is enabled.
        """
        print("Fog of war:")
        print(coloured("1. ", "black") + coloured("Enabled", "green"))
        print(coloured("2. ", "black") + coloured("Disabled", "red"))
        print()
        print("Please enter fog of war setting:")
        while True:
            fog_of_war = msvcrt.getch()
            try:
                fog_of_war = int(fog_of_war.decode("utf-8"))
                if fog_of_war == 1 or fog_of_war == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True if fog_of_war == 1 else False
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

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
            return "INVALID"
        
    def reset(self) -> None:
        """
        Reset the game state.
        """
        self.game_over = False
        self.moves = 0        