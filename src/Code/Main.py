import os
import msvcrt
from time import sleep
from termcolor import colored as coloured, cprint

if __name__ == '__main__':
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("Choose your GUI:", "cyan")
    print(coloured("1. ", "magenta") + coloured("Pygame", "yellow"))
    print(coloured("2. ", "magenta") + coloured("Terminal", "yellow"))
    print(coloured("3. ", "magenta") + coloured("Exit", "yellow"))
    print()
    print("Note:")
    print("The Terminal GUI is " + coloured("only v1.6.4", "green") + '.')
    print("It will " + coloured("NO longer ", "red", attrs=["bold"]) + "be updated!")
    print()
    
    while True:
        key = msvcrt.getch()
        if key != b'1' and key != b'2' and key != b'3': # Invalid input
            cprint("Invalid input. Please try again.", "red")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            if key == b'1':
                print("Please wait while the game is loading...")
                os.system("python src\Code\PygameGUI\MainPygame.py") 
            elif key == b'2': # Run terminal GUI (up to v1.6.3)
                os.system("python src\Code\TerminalGUI\MainTerminal.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thank you for playing!")
            print("Goodbye!")
            sleep(1)
            raise SystemExit
