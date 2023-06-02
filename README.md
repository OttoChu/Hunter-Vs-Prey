# Hunter-Vs-Prey
This is a game where you play as the Hunter and your goal is to catch the Prey in the shortest amount of turns. 

This game will be updated sometimes. To see what changed, have a look at the *update_log.txt*.

## Getting Started
Install the dependencies using following command:

    pip install -r ./dep/requirements.txt

To start the game, fun the following command:

    python ./src/main.py

***Good Luck and have fun!***

# How to Play
* Press 'WASD' to move the Hunter around.

* Press 'E' to toggle the special ability.

## Rules
1. Squares that you can be on are represented as 🌳.

2. Squares that you can **NOT** be on are represented as 🗻.

3. The Prey is represented as 👨.

4. The Hunter is represented as 🦊.

5. If an invalid move is made, your total move will be incremented by **1**.

6. You starts with 10 special moves.

7. Toggling your special move will count as a turn.

## Game Modes
You can toggle the following game modes under the settings menu:

- Fog of War (Off by default)
    - You can only see a 5x5 area around the Hunter.
    - The rest of the map is covered by fog.
    - The fog is represented as 🌫️.

*Currently there is only one game mode, but more will be added in the future.*

## Special abilities

You can choose between the following special abilities under the settings menu.

- Jumper (Default)
    - Able to move 2 tiles in the same direction in one turn.
    - This includes jumping over a mountain.
    - This ability can be used 10 times per game.

- Time Stopper
    - Allows you to stop time for 3 turns.
    - During this time, the Prey will not move.
    - This ability can be ended early by pressing 'E' again.
    - This ability can be used 5 times per game.

- Teleporter
    - Allows you to teleport to a tile on the map.
    - This is only the 8x8 area around the Hunter.
    - You can only teleport to a 🌳 tile.
    - This ability can be used once per game.

- Spotter
    - Reveal a 11x11 area around the Hunter instead of the normal 5x5.
    - This ability can be used 3 times per game.
    - This ability can only be used in Fog of War mode. (If Fog of War is off, this ability will turn Fog of War **ON**)

*More special abilities (e.g. Baiter, Spotter, Shooter) will be added in the future. Stay Tune!*

# Future Updates

1. Add a GUI (using pygame?)

2. Different types of prey (with different special moves)

3. Better AI for the prey (need to be less demanding to increase map size)

4. More types of hunter ability
    - Baiter
        - place a bait in a 5x5 area next to the Hunter on the map (except the wall)
        - the bait should be able to attract the prey to it
        - (only if the prey is close enough (distance to do set later))
    - Spotter
        - This should only be useable in fog of war mode
        - reveal a 10x10 area around the hunter instead of the normal 5x5
    - Shooter
        - shoot a bullet in a straight line in any direction
        - the bullet should be able to kill the prey if it hits it (ending game if the bullet hits the prey)