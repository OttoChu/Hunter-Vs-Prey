import pygame
from Button import Button


class GameGUI():
    '''
    The GUI class is used to create a GUI for the Hunter Vs Prey game.
    '''
    def __init__(self) -> None:
        '''
        Initializes the GUI.
        '''

        # Screen
        self.screen_size = (1200, 675) # The size of the screen
        self.screen_center = (self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Hunter vs Prey") # Sets the title of the window
        pygame.display.set_icon(pygame.image.load("src/Graphics/icon.png")) # Sets the icon of the window
        self.clock = pygame.time.Clock()

        # Flags
        self.running = True # Flag to keep track of whether the game is running or not
        self.any_key_pressed = False  # Flag to keep track of key press

        # States
        self.all_states = ["welcome", "homepage", "rules", "setting", "game", "game_over"]
        self.current_state = self.all_states[0] # The current state of the game

        # Fonts
        self.normal_font_normal = pygame.font.Font("src/Fonts/Arial.ttf", 30)
        self.normal_font_large = pygame.font.Font("src/Fonts/Arial.ttf", 50)
        self.normal_font_very_large = pygame.font.Font("src/Fonts/Arial.ttf", 75)
        self.normal_font_very_very_large = pygame.font.Font("src/Fonts/Arial.ttf", 100)
        self.normal_font_huge = pygame.font.Font("src/Fonts/Arial.ttf", 150)

        self.pixel_font_normal = pygame.font.Font("src/Fonts/Pixeltype.ttf", 30)
        self.pixel_font_large = pygame.font.Font("src/Fonts/Pixeltype.ttf", 50)
        self.pixel_font_very_large = pygame.font.Font("src/Fonts/Pixeltype.ttf", 75)
        self.pixel_font_very_very_large = pygame.font.Font("src/Fonts/Pixeltype.ttf", 100)
        self.pixel_font_huge = pygame.font.Font("src/Fonts/Pixeltype.ttf", 150)
        
    def draw_text(self, text: str, font: pygame.font.Font, colour: tuple, center_position: tuple) -> None:
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
        self.draw_text("Hunter Vs Prey!", self.pixel_font_huge, (255, 255, 255), self.screen_center)
        self.draw_text("Press any key to continue...", self.pixel_font_large, (255, 255, 255), (self.screen_center[0], self.screen_center[1] + 100))
        
        # Checks if the user has pressed any key
        if self.any_key_pressed:
            self.current_state = self.all_states[1]
            self.any_key_pressed = False
            
    def homepage(self) -> None:
        '''
        Draws the homepage of the game.
        '''

        self.draw_text("Hunter Vs Prey!", self.pixel_font_huge, (255, 255, 255), (self.screen_center[0], self.screen_center[1] - 200))

        # TODO: Add the functionality for the buttons

        new_game_button = Button((300, 150), (self.screen_center[0] - 150, self.screen_center[1] - 25), "Play", self.pixel_font_very_very_large, (0, 0, 0), (0, 255, 255), (0, 255, 0))
        new_game_button.draw(self.screen)
        rules_button = Button((200, 100), (self.screen_center[0] - 375, self.screen_center[1] + 150), "Rules", self.pixel_font_large, (0, 0, 0), (0, 255, 255), (0, 255, 0))
        rules_button.draw(self.screen)
        settings_button = Button((200, 100), (self.screen_center[0] - 100, self.screen_center[1] + 150), "Settings", self.pixel_font_large, (0, 0, 0), (0, 255, 255), (0, 255, 0))
        settings_button.draw(self.screen)
        quit_button = Button((200, 100), (self.screen_center[0] + 175, self.screen_center[1] + 150), "Quit", self.pixel_font_large, (0, 0, 0), (0, 255, 255), (0, 255, 0))
        quit_button.draw(self.screen)

        # Checks if the user has pressed any key
        if new_game_button.is_clicked():
            raise NotImplementedError
        elif rules_button.is_clicked():
            self.current_state = self.all_states[2]
        elif settings_button.is_clicked():
            self.current_state = self.all_states[3]
        elif quit_button.is_clicked():
            self.running = False
    
    def rules(self) -> None:
        '''
        Draws the rules page of the game.
        '''
        raise NotImplementedError

    def setting(self) -> None:
        '''
        Draws the setting page of the game.
        '''
        raise NotImplementedError
    
    def game(self) -> None:
        '''
        Draws the game page of the game.
        '''
        raise NotImplementedError
    
    def game_over(self) -> None:
        '''
        Draws the game over page of the game.
        '''
        raise NotImplementedError
    

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

        game_gui.screen.fill((0, 0, 100)) # Resets the screen

        # Goes to different states of the game
        if game_gui.current_state == "welcome": 
            game_gui.welcome_page()
        
        elif game_gui.current_state == "homepage":
            game_gui.homepage()

        elif game_gui.current_state == "rules":
            game_gui.rules()

        elif game_gui.current_state == "setting":
            game_gui.setting()
        
        elif game_gui.current_state == "game":
            game_gui.game()

        elif game_gui.current_state == "game_over":
            game_gui.game_over()
        
        pygame.display.update()
        game_gui.clock.tick(60)
    pygame.quit()
