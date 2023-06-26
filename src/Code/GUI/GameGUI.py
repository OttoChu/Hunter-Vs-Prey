import pygame as pg


class GameGUI():
    '''
    The GUI class is used to create a GUI for the Hunter Vs Prey game.
    '''
    def __init__(self) -> None:
        self.screen_size = (1200, 675) # The size of the screen
        self.screen_center = (self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("Hunter vs Prey") # Sets the title of the window
        pg.display.set_icon(pg.image.load("src/Graphics/icon.png")) # Sets the icon of the window
        self.clock = pg.time.Clock()

        self.all_states = ["welcome", "homepage", "game", "game_over"]
        self.current_state = self.all_states[0] # The current state of the game
        self.any_key_pressed = False  # Flag to keep track of key press

        # Fonts
        self.normal_font_normal = pg.font.Font("src/Fonts/Arial.ttf", 30)
        self.normal_font_small = pg.font.Font("src/Fonts/Arial.ttf", 20)
        self.normal_font_large = pg.font.Font("src/Fonts/Arial.ttf", 50)
        self.normal_font_very_large = pg.font.Font("src/Fonts/Arial.ttf", 100)
        self.normal_font_very_small = pg.font.Font("src/Fonts/Arial.ttf", 15)
        self.normal_font_very_very_small = pg.font.Font("src/Fonts/Arial.ttf", 10)
        self.normal_font_very_very_large = pg.font.Font("src/Fonts/Arial.ttf", 150)

        self.pixel_font_normal = pg.font.Font("src/Fonts/Pixeltype.ttf", 30)
        self.pixel_font_small = pg.font.Font("src/Fonts/Pixeltype.ttf", 20)
        self.pixel_font_large = pg.font.Font("src/Fonts/Pixeltype.ttf", 50)
        self.pixel_font_very_large = pg.font.Font("src/Fonts/Pixeltype.ttf", 100)
        self.pixel_font_very_small = pg.font.Font("src/Fonts/Pixeltype.ttf", 15)
        self.pixel_font_very_very_small = pg.font.Font("src/Fonts/Pixeltype.ttf", 10)
        self.pixel_font_very_very_large = pg.font.Font("src/Fonts/Pixeltype.ttf", 150)

    def check_quit(self, event) -> None:
        '''
        Checks if the user has quit the game.
        
        :param event:   The event that is being checked.
        '''
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        
    def draw_text(self, text: str, font: pg.font.Font, colour: tuple, center_position: tuple) -> None:
        '''
        Draws text on the screen.
        
        :param text:    The text that is being drawn.
        :param font:    The font of the text.
        :param color:   The color of the text.
        :param x:       The x coordinate of the text.
        :param y:       The y coordinate of the text.
        '''
        text_obj = font.render(text, True, colour)
        text_rect = text_obj.get_rect()
        text_rect.center = center_position
        self.screen.blit(text_obj, text_rect)

    def welcome_page(self) -> None:
        '''
        Draws the welcome page of the game.
        '''
        self.draw_text("Welcome to Hunter Vs Prey!", self.pixel_font_very_large, (255, 255, 255), self.screen_center)
        self.draw_text("Press any key to continue", self.pixel_font_normal, (255, 255, 255), (self.screen_center[0], self.screen_center[1] + 100))
        
        # Checks if the user has pressed any key
        if self.any_key_pressed:
            self.current_state = self.all_states[1]
            self.any_key_pressed = False
            
    def homepage(self) -> None:
        '''
        Draws the homepage of the game.
        '''
        # TODO: Add the homepage of the game
        # The following code is just a placeholder

        self.draw_text("Homepage", self.pixel_font_very_large, (255, 255, 255), self.screen_center)
        
        # Checks if the user has pressed any key
        if self.any_key_pressed:
            self.current_state = self.all_states[2]
            self.any_key_pressed = False

if __name__ == '__main__':
    pg.init()
    game_gui = GameGUI()  
    
    while True:
        for event in pg.event.get():
            game_gui.check_quit(event)
            
            if event.type == pg.KEYDOWN:
                game_gui.any_key_pressed = True
            elif event.type == pg.KEYUP:
                game_gui.any_key_pressed = False

        game_gui.screen.fill((0, 0, 0)) # Fills the screen with black (Resets the screen)


        # Goes to different states of the game
        if game_gui.current_state == "welcome": 
            game_gui.welcome_page()
        
        elif game_gui.current_state == "homepage":
            game_gui.homepage()

        else:
            print("Error: Invalid State!")
        
        
        
        pg.display.update()
        game_gui.clock.tick(60)
