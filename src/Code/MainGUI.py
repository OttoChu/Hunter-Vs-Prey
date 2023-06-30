import pygame
from GUI.GameGUI import *


if __name__ == '__main__':
    pygame.init()
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
        if game_gui.current_state == "welcome": 
            game_gui.welcome_page()
        
        elif game_gui.current_state == "homepage":
            game_gui.homepage()

        elif game_gui.current_state == "how_to_play":
            game_gui.how_to_play()

        elif game_gui.current_state == "setting":
            game_gui.setting()
        
        elif game_gui.current_state == "game":
            game_gui.game()

        elif game_gui.current_state == "game_over":
            game_gui.game_over()
        
        else:
            print("Error: Invalid state")


        pygame.display.update()
        game_gui.clock.tick(60)
    pygame.quit()