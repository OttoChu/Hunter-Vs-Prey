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
    while True:
        game = Game()
        if game.homepage() == 1: 
            game.rules()
        else:
            difficulty = game.ask_difficulty()

            # TODO: Toggle fog of war
            
            game_map = GameMap(20)
            h_coordinate, p_coordinate = game_map.setup_map(difficulty)
            hunter = Hunter(h_coordinate)
            prey = Prey(p_coordinate)

            game_map.print_game_state((hunter.x,hunter.y), hunter.speed, hunter.charges, game.moves)

            while not game.game_over: # Main game loop
                new_move = game.ask_move()
                new_x, new_y = hunter.x, hunter.y
                updated = True
                
                if (new_move == 'W' 
                    and hunter.y - hunter.speed > 0 and hunter.y - hunter.speed < game_map.size 
                    and not game_map.is_mountain(hunter.x, hunter.y - hunter.speed)):
                    new_y = hunter.y - hunter.speed
                elif (new_move == 'A' 
                    and hunter.x - hunter.speed > 0 and hunter.x - hunter.speed < game_map.size
                    and not game_map.is_mountain(hunter.x - hunter.speed, hunter.y)):
                    new_x = hunter.x - hunter.speed
                elif (new_move == 'S' 
                    and hunter.y + hunter.speed > 0 and hunter.y + hunter.speed < game_map.size 
                    and not game_map.is_mountain(hunter.x, hunter.y + hunter.speed)):
                    new_y = hunter.y + hunter.speed
                elif (new_move == 'D' 
                    and hunter.x + hunter.speed > 0 and hunter.x + hunter.speed < game_map.size
                    and not game_map.is_mountain(hunter.x+hunter.speed, hunter.y)):
                    new_x = hunter.x + hunter.speed
                elif new_move == 'E':
                    if not hunter.toggle():
                        print(coloured("Out of charges!", "red", attrs=["bold"]))
                else:
                    cprint("Cannot get up the mountain!", "red")
                    updated = False

                if new_x != hunter.x or new_y != hunter.y:
                    game_map.update(hunter.x, hunter.y, new_x, new_y, H)
                    hunter.set_coordinate((new_x, new_y))
                    if hunter.speed == 2:
                        hunter.charges -= 1
                    
                    if hunter.x == prey.x and hunter.y == prey.y:  # This means that the hunter has caught the prey
                        if not game.end():
                            raise SystemExit
                        updated = False

                if not game.game_over and updated:
                    if hunter.charges == 0:
                        hunter.speed = 1
                    prey.make_move(game_map, (hunter.x, hunter.y))
                    if hunter.x == prey.x and hunter.y == prey.y:
                        if not game.end():
                            raise SystemExit
                    game_map.print_game_state((hunter.x,hunter.y), hunter.speed, hunter.charges, game.moves)


if __name__ == "__main__":
    main()