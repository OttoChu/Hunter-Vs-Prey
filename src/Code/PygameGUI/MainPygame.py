import pygame
from GameGUI import GameGUI
from Game import Game

def main():
    pygame.init()
    game = Game()
    game_gui = GameGUI()
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

        # Goes to different states of the game
        if game_gui.current_state == "welcome_page": 
            game_gui.welcome_page()
        
        elif game_gui.current_state == "homepage":
            game_gui.homepage()

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
            game_gui.game()

        elif game_gui.current_state == "game_over_page":
            #TODO: Add the number of moves from the game
            temp_moves = 10
            game_gui.game_over(temp_moves)
        
        else:
            print("Error: Invalid state")


        pygame.display.update()
        game_gui.clock.tick(60)
    pygame.quit()
    raise SystemExit

if __name__ == "__main__":
    main()