import pygame

from Game import Game
from GameGUI import GameGUI
from Hunter import Hunter
from Prey import Prey
from Tiles import *

def main():
    pygame.init()
    game = Game()
    game_gui = GameGUI()

    while game_gui.running:
        # Reset all input variables
        game_gui.first_keypress = False
        game_gui.first_click = False

        # Checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_gui.running = False
            elif event.type == pygame.KEYDOWN:
                game_gui.first_keypress = True
            elif event.type == pygame.KEYUP:
                game_gui.first_keypress = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_gui.first_click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                game_gui.first_click = False

        # Draws the background and game version
        game_gui.screen.blit(game_gui.background_image, (0, 0))
        game_gui.draw_game_version()

        # Goes to different states of the game
        if game_gui.current_state == "welcome_page": 
            game_gui.welcome_page()
        
        elif game_gui.current_state == "homepage":
            play = game_gui.homepage()
            if play: # Start a new game
                game.setup_game(game.chosen_difficulty, game.chosen_ability)
                starting_hunter_pos, starting_prey_pos = game.get_animal_position()
                hunter = Hunter(starting_hunter_pos, game.chosen_ability, game.fog_of_war)
                prey = Prey(starting_prey_pos)

        elif game_gui.current_state == "how_to_play_page":
            game_gui.how_to_play()

        elif game_gui.current_state == "setting_page":
            game_gui.setting()
        
        elif game_gui.current_state == "difficulty_page":
            new_difficulty = game_gui.difficulty(game.all_difficulties[game.chosen_difficulty - 1])
            if new_difficulty != None:
                game.chosen_difficulty = new_difficulty

        elif game_gui.current_state == "fog_of_war_page":
            new_fog = game_gui.fog_of_war(game.fog_of_war)
            if new_fog != None:
                game.fog_of_war = new_fog
                if game.chosen_ability == 4:
                    game.chosen_ability = 1

        elif game_gui.current_state == "ability_page":
            new_ability = game_gui.ability(game.all_abilities[game.chosen_ability - 1])
            if new_ability != None:
                game.chosen_ability = new_ability
                if new_ability == 4:
                    game.fog_of_war = True

        elif game_gui.current_state == "game_page":
            user_move = game_gui.game(game.board, game.fog_of_war, game.moves, hunter)
            # Increment moves if user made a move
            if user_move != None and hunter.moves_on_turn == 1 and user_move != 'E' or (game_gui.first_keypress and user_move != 'E'):
                game.moves += 1
            # Check if user choose to use ability
            if user_move == 'E':
                # Toggle special ability
                if hunter.special_status:
                    hunter.reset_settings()
                else:
                    if hunter.charges > 0:
                        hunter.special_status = True
                    else:
                        game.moves += 1

                # Do special ability if hunter has enough charges
                if hunter.special_status:
                    if hunter.special_ability == "Jumper":
                        hunter.speed = 2
                    elif hunter.special_ability == "Time Stopper":
                        hunter.charges -= 1
                        hunter.moves_on_turn = 4
                    elif hunter.special_ability == "Teleporter":
                        hunter.charges -= 1
                        game_gui.current_state = "choose_teleport_page"
                    elif hunter.special_ability == "Spotter":
                        hunter.charges -= 1
                        hunter.visibility = 5

            # Check if user choose to move hunter
            elif user_move == 'W' and game.board_size > hunter.y > 0 and not game.is_mountain((hunter.x, hunter.y - hunter.speed)):
                game.update_board((hunter.get_position()), (hunter.x, hunter.y - hunter.speed), H)
                hunter.set_coordinate((hunter.x, hunter.y - hunter.speed))
            elif user_move == 'A' and game.board_size > hunter.x > 0 and not game.is_mountain((hunter.x - hunter.speed, hunter.y)):
                game.update_board((hunter.get_position()), (hunter.x - hunter.speed, hunter.y), H)
                hunter.set_coordinate((hunter.x - hunter.speed, hunter.y))
            elif user_move == 'S' and game.board_size > hunter.y > 0 and not game.is_mountain((hunter.x, hunter.y + hunter.speed)):
                game.update_board((hunter.get_position()), (hunter.x, hunter.y + hunter.speed), H)
                hunter.set_coordinate((hunter.x, hunter.y + hunter.speed))
            elif user_move == 'D' and game.board_size > hunter.x > 0 and not game.is_mountain((hunter.x + hunter.speed, hunter.y)):
                game.update_board((hunter.get_position()), (hunter.x + hunter.speed, hunter.y), H)
                hunter.set_coordinate((hunter.x + hunter.speed, hunter.y))

            # Reset special ability if hunter has completed the move
            if hunter.special_status and user_move != None and user_move != 'E':
                hunter.special_status = False
                if hunter.special_ability == "Jumper":
                    hunter.charges -= 1
                    hunter.special_status = False
                    hunter.reset_settings()
                elif hunter.special_ability == "Time Stopper":
                    hunter.moves_on_turn -= 1
                    if hunter.moves_on_turn > 1:
                        hunter.special_status = True
                elif hunter.special_ability == "Spotter":
                    hunter.reset_settings()
                       
            if hunter.get_position() == prey.get_position():
                game_gui.current_state = "game_over_page"

            # Move prey
            else:
                # TODO: Make the prey move after the hunter has moved
                #       Only move the prey if the hunter is moved and not game over
                pass
            #       If yes, game over
            #       If no, move prey
        
        elif game_gui.current_state == "choose_teleport_page":
            new_coordinates = game_gui.choose_teleport(game.board, hunter.get_position(), game.fog_of_war)
            if new_coordinates != None:
                if new_coordinates[-1]:
                    game.update_board((hunter.get_position()), new_coordinates, H)
                    hunter.set_coordinate(new_coordinates)
                hunter.special_status = False
                game_gui.current_state = "game_page"

        elif game_gui.current_state == "game_over_page":
            again = game_gui.game_over(game.moves)
            if again:
                game.setup_game(game.chosen_difficulty, game.chosen_ability)
                starting_hunter_pos, starting_prey_pos = game.get_animal_position()
                hunter = Hunter(starting_hunter_pos, game.chosen_ability, game.fog_of_war)
                prey = Prey(starting_prey_pos)
        
        pygame.display.update()
        game_gui.clock.tick(60)
        
    pygame.quit()
    raise SystemExit

if __name__ == "__main__":
    main()