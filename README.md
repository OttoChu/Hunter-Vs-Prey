# Hunter-Vs-Prey
This is a game where you play as the Hunter and your goal is to catch the Prey in the shortest amount of turns. 

This game will be updated sometimes. To see what changed, have a look at the *update_log.txt*.

## Getting Started
Install the dependencies using following command:

    pip install -r ./dep/requirements.txt

***Good Luck and have fun!***

# How to Play
* Press 'WASD' to move the Hunter around.

* Press 'E' to toggle the special move.

## Rules
1. The Prey is represented as 🦊.

2. The Hunter is represented as 👨.

3. Both the Hunter and Prey can move 1 square at a time..

4. The squares that you can be on are represented as 🌳.

5. The squares that you can NOT be on are represented as 🗻.

6. If an invalid move is made, your total moves count will be incremented by 1!

7. "You start with 10 special moves

8. Toggling your special move will count as a turn.

# Future Updates

1. Add a GUI (using pygame?)

2. Different types of prey (with different special moves)

3. More types of hunter ability
    - Teleporter
        - teleport to any tile on the map (except the wall)
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