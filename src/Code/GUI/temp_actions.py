# This file is used to test the GUI class and its methods

import pygame as pg
from GUI import GUI


if __name__ == '__main__':
    pg.init()
    game_gui = GUI((1200, 675), "Hunter vs Prey")
    is_key_pressed = False  # Flag to keep track of key press
    all_states = ["homepage", "game", "game_over"]
    current_state = all_states[0] # The current state of the game
    
    while True:
        for event in pg.event.get():
            game_gui.check_quit(event)
            
            if event.type == pg.KEYDOWN:
                is_key_pressed = True
            elif event.type == pg.KEYUP:
                is_key_pressed = False

        game_gui.screen.fill((0, 0, 0))
        screen_center_x = game_gui.screen_size_x // 2
        screen_center_y = game_gui.screen_size_y // 2
        
        if pg.mouse.get_pressed()[0]:
            game_gui.draw_text("You clicked the mouse!", game_gui.font, (255, 255, 255), screen_center_x, screen_center_y)
        elif pg.key.get_pressed()[pg.K_SPACE]:
            game_gui.draw_text("You pressed the space bar!", game_gui.font, (255, 255, 255), screen_center_x, screen_center_y)
        elif is_key_pressed:
            game_gui.draw_text("You are holding down a key!", game_gui.font, (255, 255, 255), screen_center_x, screen_center_y)
        else:
            game_gui.draw_text("Welcome to Hunter Vs Prey!", game_gui.font, (255, 255, 255), screen_center_x, screen_center_y)
        
        pg.display.update()
        game_gui.clock.tick(60)
