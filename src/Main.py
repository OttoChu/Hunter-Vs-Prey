# Hunter Vs Prey v1.5.0

import os
from termcolor import cprint, colored as coloured

from Tiles import *
from Game import Game
from GameMap import GameMap
from Animals.Hunter import Hunter
from Animals.Prey import Prey


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
            # Start a new game
            game_map = GameMap(15)
            h_coordinate, p_coordinate = game_map.setup_map(game.difficulty)
            hunter = Hunter(h_coordinate)
            prey = Prey(p_coordinate)
            game_map.print_game_state((hunter.x,hunter.y), hunter.special_status, hunter.charges, 1, game.fog_of_war, hunter.moves_on_turn)

            while not game.game_over: # Main game loop
                if hunter.moves_on_turn == 1:
                    game.moves += 1
                
                # Hunter's turn
                activate = False
                for moves_left in range(hunter.moves_on_turn):
                    charge_error, mountain_error, input_error = False, False, False
                    new_move = game.ask_move()
                    new_x, new_y = hunter.x, hunter.y
                    if not (new_move == 'W' or new_move == 'A' or new_move == 'S' or new_move == 'D' or new_move == 'E'):
                        input_error = True
                    elif new_move == 'E':
                        if not hunter.toggle_special_move():
                            charge_error = True
                        if hunter.special_status:
                            activate = True
                            if hunter.moves_on_turn != 0:
                                hunter.charges -= 1
                                moves_left += 1
                        else:
                            break

                    else:
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
                        else:
                            mountain_error = True
                    
                    # Update the game state if the hunter has moved
                    if new_x != hunter.x or new_y != hunter.y:
                        game_map.update(hunter.x, hunter.y, new_x, new_y, H)
                        hunter.set_coordinate((new_x, new_y))
            
                    # Check if the hunter has caught the prey
                    if hunter.x == prey.x and hunter.y == prey.y:
                        game.game_over = True
                        break
                    
                    # Print the game state
                    if not game.game_over:
                        
                        temp =  hunter.moves_on_turn - moves_left
                        # TODO: Fix 3 moves in the same turn bug
                        # It currently only gives 2 moves when first activated and 3 after that
                        # This is because the first time it is activated, the for loop value is 0
                        # aka activate takes 1 move and only 2 moves are left



                        # if temp == 0 and hunter.special_status == False:
                        #     hunter.charges -= 1

                        game_map.print_game_state((hunter.x,hunter.y), hunter.special_status, hunter.charges, game.moves, 
                                                  game.fog_of_war, temp,
                                                  charge_error, mountain_error, input_error)
                        # print(hunter.special_status)

                # Prey's turn
                if not game.game_over:
                    if hunter.special_status and not activate: 
                        hunter.charges -= 1
                    if hunter.charges <= 0:
                        hunter.default_settings()
                    prey.make_move(game_map, (hunter.x, hunter.y)) # The prey makes a move

                    game_map.print_game_state((hunter.x,hunter.y), hunter.special_status, hunter.charges, game.moves, 
                                                  game.fog_of_war, temp,
                                                  charge_error, mountain_error, input_error)

                    if hunter.x == prey.x and hunter.y == prey.y:
                        if not game.end():
                            raise SystemExit
                    
            # The game is over      
            if game.game_over:
                if not game.end():
                    raise SystemExit
                game.game_over = False


if __name__ == "__main__":
    main()