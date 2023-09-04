# Hunter-Vs-Prey
This is a game where you play as the Hunter and your goal is to catch the Prey in the shortest amount of turns. 

This game will be updated sometimes. To see what changed, have a look at the *update_log.txt* under the folder named *"docs"*.

From v2.0.1 onwards, the game will be using a GUI made with Pygame. The terminal version of the game will no longer be updated. If you want to play the terminal version of the game, you will have to run the executable file named *"HunterVsPrey_v1.6.4.exe"*.

**Additional note: This game is built using Python 3.8.10. It might not work on other versions of Python.**

## Getting Started

### For those who want to play without installing Python and the dependencies (aka lazy and trust me)

To start the game, you can run the executable file named ***"HunterVsPrey_vXX.exe"*** where "*XX*" is the version number of the game.
*Note: v1.6.4 is the last terminal based version of the game.*

### For those who don't trust the executable file

Install the dependencies using the following command:

    pip install -r .\dep\requirements.txt

To start the game, you can run the following command:

    python .\src\Main.py


***Good Luck and have fun!***

## How to Play
- Press *'WASD'* or *arrow keys* to move the Hunter around.

- Press *'E'*  or *right shift* to toggle the special ability.

- You may also use the on-screen buttons to move and toggle the special ability. ***(Only available with the Pygame GUI)***

### Rules
1. The Hunter is represented as 🦊.

2. The Prey is represented as 👨.

3. Fog is represented as 🌫️.

4. Both the Hunter and Prey can move 1 tile in any direction per turn (excluding diagonals).

5. Squares that you can be on are represented as 🌳.

6. Squares that you can **NOT** be on are represented as 🗻.

7. If an invalid move is made, your total move will be incremented by **1**.

### Game Modes

You can toggle the following game modes under the settings menu:

- Fog of War (**OFF** by default)
    - You can only see a 5x5 area around the Hunter.
    - The rest of the map is covered by fog.
    - The fog is represented as 🌫️.

*Currently, there is only one game mode, but more will be added in the future. Feel free to suggest new game modes!*

### Special abilities

You can choose between the following special abilities under the settings menu.

- Jumper (**Default**)

    - Moves 2 tiles in the same direction in one turn.
    - This includes jumping over a mountain.
    - This ability can be used 10 times per game.

- Time Stopper

    - Makes 3 moves in the same turn.
    - During this time, the Prey will not move.
    - This ability can be ended early by pressing the ability key again.
    - This ability can be used 5 times per game.

- Teleporter
    - Teleports to a chosen tile on the map.
    - This is only the 9x9 area around the Hunter.
    - You can only teleport to a 🌳 tile.
    - This ability can be used once per game.

- Spotter

    - Reveals an 11x11 area around the Hunter instead of the normal 5x5 in Fog of War game mode.
    - This ability can be used 3 times per game.
    - This ability can only be used in Fog of War mode. (If Fog of War is off, this ability will turn Fog of War **ON**)

*More special abilities will be added in the future. Stay Tune!*

## Bugs
*The following are bugs that I know of. If you find any other bugs, please let me know.*

### PygameGUI

*None so far! :)*

### TerminalGUI

1. When Fog of War is enabled, the Teleporter ability removes the fog activated.

See bugs.txt *(\docs\bugs.txt)* for more details.

## Future Updates
*The following are only plans. There might be changes to the finer details.*

1. Different types of prey (with different special moves)

2. Better AI for the prey (need to be less demanding to increase map size)

    - Could use Markov Decision Process (MDP) to make the prey smarter (maybe look into this)

    - Could use Reinforcement Learning (RL) to make the prey smarter (long-term goal)

3. More types of hunter ability
    - Baiter
        - place a bait in a 5x5 area next to the Hunter on the map (except the wall)
        - the bait should be able to attract the prey to it
        - (only if the prey is close enough (distance to do set later))
    - Shooter
        - shoot a bullet in a straight line in any direction
        - the bullet should be able to kill the prey if it hits it (ending game if the bullet hits the prey)

4. More game modes
    - Multiple Prey
        - there will be more than one prey on the map
        - the hunter will have to catch all the prey to win
        
6. Add a database
    - need to have different accounts
    - can play as a guest (no account needed)
    - save game for later
    - to store the best score of each game mode
    - to store achievements (e.g. fastest win, most turns taken, etc.)
    - a leaderboard for each game mode to compare with other players

7. Add a shop (Only after a database is implemented)
    - to buy new abilities
    - to buy  or unlock new skins for the hunter and prey 

8. Add a tutorial
    - to teach new players how to play the game
