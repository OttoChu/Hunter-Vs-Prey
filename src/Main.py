# Hunter Vs Prey v1.6.3

import os

from Tiles import *
from Game import Game
from GameMap import GameMap
from Animals.Hunter import Hunter
from Animals.Prey import Prey

def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    game = Game()
    while True:
        option = game.homepage()
        if option == 2: 
            game.rules()
        elif option == 3:
            while True:
                setting_option = game.settings()
                if setting_option == 1:
                    while True:
                        if game.choose_difficulty() == 7:
                            break
                elif setting_option == 2:
                    while True:
                        if game.choose_fog_of_war() == 3:
                            break
                elif setting_option == 3:
                    while True:
                        if game.choose_special_ability() == 5:
                            break
                elif setting_option == 4:
                    break
        elif option == 4:
            raise SystemExit
        else:
            # Start a new game
            game_map = GameMap(15)
            h_coordinate, p_coordinate = game_map.setup_map(game.chosen_difficulty)
            hunter = Hunter(h_coordinate, game.chosen_ability)
            prey = Prey(p_coordinate)
            game_map.print_game_map(hunter.get_position(), game.fog_of_war, hunter.special_ability, hunter.special_status)
            game_map.print_state_description(hunter.special_status, hunter.charges, 1, 1,
                hunter.special_ability)

            while not game.game_over: # Main game loop
                if hunter.moves_on_turn == 1:
                    game.moves += 1
                # Hunter's turn
                activate = False
                moves_left_calculation = 1
                moves_this_turn = hunter.moves_on_turn
                for moves_left in range(moves_this_turn): # Loop for the number of moves the hunter can make this turn
                    charge_error, mountain_error, input_error = False, False, False
                    new_move = game.ask_move()
                    new_x, new_y = hunter.get_position()
                    if not (new_move == 'W' or new_move == 'A' or new_move == 'S' or new_move == 'D' or new_move == 'E'):
                        input_error = True
                    elif new_move == 'E':
                        if not hunter.toggle_special_move():
                            charge_error = True
                        if hunter.special_status:
                            activate = True
                            if hunter.special_ability == "Teleporter": # teleporting the hunter
                                hunter.charges -= 1
                                new_pos, change = game.ask_teleport_location(game_map.game_map, hunter.get_position())
                                if change: # only update the hunter position if the user did not cancel the teleport
                                    game_map.update(hunter.x, hunter.y, new_pos[0], new_pos[1], H)
                                    hunter.set_coordinate(new_pos)
                                    break
                        else:
                            if hunter.special_ability == "Time Stopper" or hunter.special_ability == "Spotter": # turning off the ability before using all the moves
                                hunter.charges -= 1
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
                    # Print the game state if the game is not over
                    if not game.game_over:
                        # Calculate the number of moves left on the turn
                        if hunter.special_ability == 'Time Stopper':
                            if hunter.special_status:
                                if activate:
                                    moves_left_calculation = 3
                                else:
                                    temp_calculation = hunter.moves_on_turn - moves_left - 1
                                    moves_left_calculation = 1 if temp_calculation == 0 else temp_calculation
                            else:
                                moves_left_calculation = 1
                        game_map.print_game_map(hunter.get_position(), game.fog_of_war, hunter.special_ability, hunter.special_status)
                        game_map.print_state_description(hunter.special_status, hunter.charges, game.moves, 
                            moves_left_calculation, hunter.special_ability, charge_error, mountain_error, input_error)

                # Prey's turn
                if not game.game_over:
                    # Continuing the special ability
                    if hunter.special_status and not activate: 
                        if hunter.special_ability == 'Time Stopper' or hunter.special_ability == 'Spotter':
                            hunter.toggle_special_move()
                        hunter.charges -= 1
                    # Resetting the special ability when the charges run out
                    if hunter.charges <= 0:
                        hunter.default_settings()
                    prey.make_move(game_map, hunter.get_position()) # The prey makes a move
                    game_map.print_game_map(hunter.get_position(), game.fog_of_war, hunter.special_ability, hunter.special_status)
                    game_map.print_state_description(hunter.special_status, hunter.charges, game.moves, 
                        moves_left_calculation, hunter.special_ability, charge_error, mountain_error, input_error)

            # The game is over      
            if game.game_over:
                if not game.end():
                    raise SystemExit
                game.reset()

if __name__ == "__main__":
    main()