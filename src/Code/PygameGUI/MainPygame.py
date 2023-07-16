import pygame

from Game import Game
from GameGUI import GameGUI
from Hunter import Hunter
from Prey import Prey
from Tiles import *

def main():
    pygame.init()
    pygame.key.set_repeat()
    game = Game()
    game_gui = GameGUI()

    # game.setup_board(game.chosen_difficulty)
    
    


    while game_gui.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_gui.running = False
            elif event.type == pygame.KEYDOWN:
                game_gui.any_key_pressed = True
                
            elif event.type == pygame.KEYUP:
                game_gui.any_key_pressed = False
        
        game_gui.first_click = game_gui.is_first_click()

        # Checks if the mouse is held down
        if not any(pygame.mouse.get_pressed()):
            game_gui.mouse_held = False

        game_gui.screen.blit(game_gui.background_image, (0, 0)) # Draws the background
        game_gui.draw_game_version() # Draws the game version

        # Goes to different states of the game
        if game_gui.current_state == "welcome_page": 
            game_gui.welcome_page()
        
        elif game_gui.current_state == "homepage":
            play = game_gui.homepage()
            if play:
                game.setup_game(game.chosen_difficulty, game.chosen_ability)
                starting_hunter_pos, starting_prey_pos = game.get_animal_position()
                hunter = Hunter(starting_hunter_pos, game.chosen_ability)
                prey = Prey(starting_prey_pos)

        elif game_gui.current_state == "how_to_play_page":
            game_gui.how_to_play()

        elif game_gui.current_state == "setting_page":
            game_gui.setting()
        
        elif game_gui.current_state == "difficulty_page":
            game_gui.difficulty()

        elif game_gui.current_state == "fog_of_war_page":
            game_gui.fog_of_war()

        elif game_gui.current_state == "ability_page":
            game_gui.ability()

        elif game_gui.current_state == "game_page":
            user_move = game_gui.game(game.board, H, game.moves, hunter)
            # Increment moves if user made a move
            if user_move != None:
                game.moves += 1
            # Check if user choose to use ability
            if user_move == 'E':
                # Toggle special ability
                if hunter.special_status: # disable special ability
                    hunter.special_status = False
                else: # enable special ability
                    # TODO: decrement charges if hunter keep using special ability aka jumper ability
                    if hunter.charges > 0:
                        hunter.special_status = True
                        hunter.charges -= 1

                # Do special ability
                if hunter.special_ability == "Jumper":
                    pass

                
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


            # TODO: Check if hunter is on prey
            if hunter.get_position() == prey.get_position():
                game_gui.current_state = "game_over_page"
            #       If yes, game over
            #       If no, move prey


        elif game_gui.current_state == "game_over_page":
            again = game_gui.game_over(game.moves)
            if again:
                game.setup_game(game.chosen_difficulty, game.chosen_ability)
                starting_hunter_pos, starting_prey_pos = game.get_animal_position()
                hunter = Hunter(starting_hunter_pos, game.chosen_ability)
                prey = Prey(starting_prey_pos)
        
        pygame.display.update()
        game_gui.clock.tick(60)
        
    pygame.quit()
    raise SystemExit

if __name__ == "__main__":
    main()