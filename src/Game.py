import msvcrt
import os
from termcolor import cprint, colored as coloured

class Game:
    """
    The main class that runs the game.
    """
    def __init__(self):
        """
        Initialize the game.
        """
        self.game_over = False # A boolean that indicates whether the game is over or not.
        self.moves = 0 # The number of moves the player has made.
    
    def homepage(self) -> int:
        """
        Print the homepage onto the screen. Ask for input for what to show next.

        :return: A number between 1 - 3 representing the chosen option.
        """
        cprint("Welcome to Hunter Vs Prey!", "green", attrs=["bold"])
        print()
        cprint("How to win?", "blue")
        cprint("The goal of this game is to get the hunter to the prey.", "blue")
        print()
        print(coloured("1. ", "black") + coloured("Rules", "yellow"))
        print(coloured("2. ", "black") + coloured("Toggle Game Modes", "yellow"))
        print(coloured("3. ", "black") + coloured("New Game", "yellow"))
        print(coloured("4. ", "black") + coloured("Quit", "yellow"))
        print()
        while True:
            option = msvcrt.getch()
            try:
                option = int(option.decode("utf-8"))
                if option >= 1 and option <= 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if option == 4:
                        print("Thank you for playing!")
                        raise SystemExit
                    return option
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")

    def rules(self) -> None:
        """
        Print all the rules onto the screen.
        """
        print("Rules")
        print("1. Squares that you can be on are represented as 🌳.")
        print("2. Squares that you can **NOT** be on are represented as 🗻.")
        print("3. The Prey is represented as 👨.")
        print("4. The Hunter is represented as 🦊.")
        print("5. If an invalid move is made, your total move will be " + coloured("incremented by 1", "red") + "!")
        print("6. You starts with 10 special moves.")
        print("7. Toggling your special move will count as a turn.")
        print()
        print('Here are the accepted inputs:')
        cprint("'W' to move upwards", 'red')
        cprint("'A' to move to the left", 'blue')
        cprint("'S' to move downwards", 'yellow')
        cprint("'D' to move to the right", 'magenta')
        print()
        cprint("'E' to toggle the special move", "green")
        print()
        cprint("Press anything to return to the homepage.", "black")
        _ = msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')

    def end(self) -> bool:
        """
        Print the end screen onto the screen. Ask for input for whether to play again.

        :return: A boolean that indicates whether the player wants to play again.
        """
        self.game_over = True
        os.system('cls' if os.name == 'nt' else 'clear')
        cprint("The hunter has eaten the prey!", "green", "on_red")
        cprint(" __     ______  _    _  __          _______ _   _   _ \n \ \   / / __ \| |  | | \ \        / /_   _| \ | | | |\n  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | | |\n   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | | |\n    | | | |__| | |__| |    \  /\  /   _| |_| |\  | |_|\n    |_|  \____/ \____/      \/  \/   |_____|_| \_| (_)\n", "red")
        print(f"You caught the prey in {self.moves} moves")
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
            cprint("Wrong input! Try again!", "red")

    def ask_difficulty(self) -> int:
        """
        Ask the user for the game difficulty.
        
        :return: A number between 1 - 5 representing the chosen difficulty.
        """
        print("Game difficulties:")
        print(coloured("1. ", "black") + coloured("Extra Easy", "cyan"))
        print(coloured("2. ", "black") + coloured("Easy", "light_blue"))
        print(coloured("3. ", "black") + coloured("Normal", "light_yellow"))
        print(coloured("4. ", "black") + coloured("Hard", "light_red"))
        print(coloured("5. ", "black") + coloured("Extra Hard", "light_magenta"))
        print()
        print("Please enter game difficulty:")
        while True:
            difficulty = msvcrt.getch()
            try:
                difficulty = int(difficulty.decode("utf-8"))
                if difficulty > 0 and difficulty <= 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return difficulty
            except (UnicodeDecodeError, ValueError):
                pass
            cprint("Invalid input!", "red")
            
    def ask_move(self) -> str:
        """
        Ask the user for the next move.
        """
        while True:
            move = msvcrt.getch()
            try:
                move = move.decode("utf-8").upper()
                if move == 'W' or move == 'A' or move == 'S' or move == 'D' or move == 'E':
                    self.moves += 1
                    return move
            except UnicodeDecodeError:
                pass
            cprint("Wrong input! Try again!", "red")