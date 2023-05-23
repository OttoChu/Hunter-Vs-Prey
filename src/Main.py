# Hunter Vs Prey v1.5.0

import os
from termcolor import cprint, colored as coloured

from Tiles import *
from Game import Game
from GameMap import GameMap
from Hunter import Hunter
from Prey import Prey


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    game = Game()
    while True:
        
        option = game.homepage()
        if option == 2: 
            game.rules()
        elif option == 3:
            # TODO: Implement the settings menu including the ability to change the difficulty and toggle the fog
            while True:
                setting_option = game.settings()
                if setting_option == 1:
                    while True:
                        if game.choose_difficulty() == 6:
                            break
                elif setting_option == 2:
                    while True:
                        if game.choose_fog_of_war() == 3:
                            break
                elif setting_option == 3:
                    break
        elif option == 4:
            raise SystemExit
        else:
            game_map = GameMap(15)
            h_coordinate, p_coordinate = game_map.setup_map(game.difficulty)
            hunter = Hunter(h_coordinate)
            prey = Prey(p_coordinate)
            game_map.print_game_state((hunter.x,hunter.y), hunter.speed, hunter.charges, game.moves, game.fog_of_war)

            while not game.game_over: # Main game loop
                new_move = game.ask_move()
                new_x, new_y = hunter.x, hunter.y
                if (new_move == 'W' 
                    and hunter.y - hunter.speed > 0 and hunter.y - hunter.speed < game_map.size 
                    and not game_map.is_mountain(hunter.x, hunter.y - hunter.speed)): # If the hunter can move up
                    new_y = hunter.y - hunter.speed
                elif (new_move == 'A' 
                    and hunter.x - hunter.speed > 0 and hunter.x - hunter.speed < game_map.size
                    and not game_map.is_mountain(hunter.x - hunter.speed, hunter.y)): # If the hunter can move left
                    new_x = hunter.x - hunter.speed
                elif (new_move == 'S' 
                    and hunter.y + hunter.speed > 0 and hunter.y + hunter.speed < game_map.size 
                    and not game_map.is_mountain(hunter.x, hunter.y + hunter.speed)): # If the hunter can move down
                    new_y = hunter.y + hunter.speed
                elif (new_move == 'D' 
                    and hunter.x + hunter.speed > 0 and hunter.x + hunter.speed < game_map.size
                    and not game_map.is_mountain(hunter.x+hunter.speed, hunter.y)): # If the hunter can move right
                    new_x = hunter.x + hunter.speed
                elif new_move == 'E':
                    if not hunter.toggle():
                        print(coloured("Out of charges!", "red", attrs=["bold"]))
                else:
                    cprint("Cannot get up the mountain!", "red")

                if new_x != hunter.x or new_y != hunter.y: # If the hunter has moved, then update the game state
                    game_map.update(hunter.x, hunter.y, new_x, new_y, H)
                    hunter.set_coordinate((new_x, new_y))
                    if hunter.speed == 2: # If the hunter used a special charge, then decrement the number of charges
                        hunter.charges -= 1
                    if hunter.x == prey.x and hunter.y == prey.y:  # This means that the hunter has caught the prey
                        game.game_over = True
                        
                if not game.game_over: # If the game is not over, then the prey makes a move
                    if hunter.charges == 0:
                        hunter.speed = 1
                    prey.make_move(game_map, (hunter.x, hunter.y))
                    if hunter.x == prey.x and hunter.y == prey.y:
                        if not game.end():
                            raise SystemExit
                    game_map.print_game_state((hunter.x,hunter.y), hunter.speed, hunter.charges, game.moves, game.fog_of_war)
                
            if game.game_over: # Ask the user if they want to play again
                if not game.end():
                    raise SystemExit
                game.game_over = False


if __name__ == "__main__":
    main()