import pygame
try:
    from Button import Button
except ModuleNotFoundError:
    # TODO: Keep this only after the game is finished
    from GUI.Button import Button

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

        # States
        self.all_states = ["welcome", "homepage", "how_to_play", "setting", "game", "game_over"]
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

        # Colours
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        # Graphics
        self.icon_image = pygame.image.load("src/Graphics/icon.png")
        self.background_image = pygame.transform.scale(pygame.image.load("src/Graphics/background.png"), self.screen_size)
        self.hunter_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/hunter.png"), (30, 30))
        self.prey_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/prey.png"), (30, 30))
        self.tree_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/tree.png"), (30, 30))
        self.mountain_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/mountain.png"), (30, 30))
        self.fog_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/fog.png"), (30, 30))
        
        # Window settings
        pygame.display.set_caption("Hunter vs Prey") # Sets the title of the window
        pygame.display.set_icon(self.icon_image) # Sets the icon of the window
        self.clock = pygame.time.Clock()

        # Random
        self.running = True # Flag to keep track of whether the game is running or not
        self.any_key_pressed = False  # Flag to keep track of key press
        self.first_click = False # Flag to keep track of whether the current mouse press is the first time
        self.mouse_held = False # Flag to keep track of whether the mouse is held or not
        self.wait_counter = 0 # Counter used to keep track of how long the frames has passed
        self.current_how_to_play_page = 1 # The current page of the how to play section
        
    def is_first_click(self) -> bool:
        '''
        Checks if the current mouse press is the first one.
        Prevents the user from creating unwanted inputs.

        :return:    True if the current mouse press is the first one, False otherwise.
        '''
        if any(pygame.mouse.get_pressed()):
            if self.mouse_held == False:
                self.mouse_held = True
                return True
            self.mouse_held = True
        return False

    def draw_text_center(self, text: str, font: pygame.font.Font, colour: tuple, center_position: tuple) -> pygame.Rect:
        '''
        Draws text on the screen.
        
        :param text:    The text that is being drawn.
        :param font:    The font of the text.
        :param color:   The color of the text.
        :param center_position: The center position of the text.

        :return:        The rectangle of the text.
        '''
        text_obj = font.render(text, True, colour)
        text_rect = text_obj.get_rect()
        text_rect.center = center_position
        self.screen.blit(text_obj, text_rect)
        return text_rect

    def draw_text_topleft(self, text: str, font: pygame.font.Font, colour: tuple, topleft_position: tuple) -> pygame.Rect:
        '''
        Draws text on the screen.
        
        :param text:    The text that is being drawn.
        :param font:    The font of the text.
        :param color:   The color of the text.
        :param x:       The x coordinate of the text.
        :param y:       The y coordinate of the text.

        :return:        The rectangle of the text.
        '''
        text_obj = font.render(text, True, colour)
        text_rect = text_obj.get_rect()
        text_rect.topleft = topleft_position
        self.screen.blit(text_obj, text_rect)
        return text_rect

    def welcome_page(self) -> None:
        '''
        Draws the welcome page of the game.
        '''
        dot_counter = self.wait_counter // 20
        self.wait_counter += 1
        if dot_counter > 3:
            dot_counter = 0
            self.wait_counter = 0
        self.draw_text_center("Hunter Vs Prey!", self.pixel_font_huge, self.white, self.screen_center)
        self.draw_text_center("Press any key to continue"+ '.' * dot_counter, self.pixel_font_large, (255, 255, 255), (self.screen_center[0], self.screen_center[1] + 100))
        
        # Checks if the user has pressed any key
        if self.any_key_pressed or (any(pygame.mouse.get_pressed()) and self.first_click):
            self.current_state = self.all_states[1]
            self.any_key_pressed = False
            self.wait_counter = 0
            
    def homepage(self) -> None:
        '''
        Draws the homepage of the game.
        '''
        self.draw_text_center("Hunter Vs Prey!", self.pixel_font_huge, self.white, (self.screen_center[0], self.screen_center[1] - 200))
        new_game_button = Button((300, 150), (self.screen_center[0] - 150, self.screen_center[1] - 25), "Play", self.pixel_font_very_very_large)
        new_game_button.draw(self.screen)
        how_to_play_button = Button((200, 100), (self.screen_center[0] - 375, self.screen_center[1] + 150), "How to play", self.pixel_font_large)
        how_to_play_button.draw(self.screen)
        settings_button = Button((200, 100), (self.screen_center[0] - 100, self.screen_center[1] + 150), "Settings", self.pixel_font_large)
        settings_button.draw(self.screen)
        quit_button = Button((200, 100), (self.screen_center[0] + 175, self.screen_center[1] + 150), "Quit", self.pixel_font_large)
        quit_button.draw(self.screen)

        # Checks if the user has pressed any key
        if new_game_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[4]
        elif how_to_play_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[2]
        elif settings_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[3]
        elif quit_button.is_clicked() and self.first_click:
            self.running = False
    
    def how_to_play(self) -> None:
        '''
        Draws the how to play pages of the game.
        '''
        # Draws the different pages of the how to play section
        self.draw_text_center("How to play", self.pixel_font_huge, self.white, (self.screen_center[0], self.screen_center[1] - 250))
        if self.current_how_to_play_page == 1: # Page 1
            self.draw_text_topleft("Goal", self.pixel_font_very_large, self.white, (100, self.screen_center[1] - 150))
            self.draw_text_topleft("- Hunter Vs Prey is a game where you play as a hunter and you have to", self.normal_font_normal, self.white, (100, self.screen_center[1] - 100))
            self.draw_text_topleft("  catch the prey", self.normal_font_normal, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- The prey is controlled by an AI and will try to run away from you", self.normal_font_normal, self.white, (100, self.screen_center[1]))
            self.draw_text_topleft("- The game will end when the Hunter is on the same tile as the Prey", self.normal_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.draw_text_center("Good luck!", self.pixel_font_large, self.green, (self.screen_center[0], self.screen_center[1] + 150))
        
        elif self.current_how_to_play_page == 2: # Page 2
            self.draw_text_topleft("Controls", self.pixel_font_very_large, self.white, (100, self.screen_center[1] - 150))
            self.draw_text_topleft("- Press 'WASD' to move", self.normal_font_normal, self.white, (100, self.screen_center[1] - 100))
            self.draw_text_topleft("- Press 'E' to use ability", self.normal_font_normal, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- You may also use the on-screen buttons to move and use ability", self.normal_font_normal, self.white, (100, self.screen_center[1] + 50))
        
        elif self.current_how_to_play_page == 3: # Page 3
            self.draw_text_topleft("Rules", self.pixel_font_very_large, self.white, (100, self.screen_center[1] - 150))
            prey_rect = self.draw_text_topleft("- The Prey is represented as", self.normal_font_normal, self.white, (100, self.screen_center[1] - 100))
            self.screen.blit(self.prey_image_small, (prey_rect.topright[0] + 10, prey_rect.topright[1]))
            hunter_rect = self.draw_text_topleft("and the Hunter is represented as", self.normal_font_normal, self.white, (prey_rect.topright[0] + 50, prey_rect.topright[1]))
            self.screen.blit(self.hunter_image_small, (hunter_rect.topright[0] + 10, hunter_rect.topright[1]))
            fog_rect = self.draw_text_topleft("- Fog are represented as", self.normal_font_normal, self.white, (100, self.screen_center[1] - 50))
            self.screen.blit(self.fog_image_small, (fog_rect.topright[0] + 10, fog_rect.topright[1]))
            self.draw_text_topleft("- All animals can move 1 tile in any direction per turn (excluding diagonals)", self.normal_font_normal, self.white, (100, self.screen_center[1]))
            tree_rect = self.draw_text_topleft("- The squares that you can be on are represented as", self.normal_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.screen.blit(self.tree_image_small, (tree_rect.topright[0] + 10, tree_rect.topright[1]))
            mountain_rect = self.draw_text_topleft("- The squares that you can NOT be on are represented as", self.normal_font_normal, self.white, (100, self.screen_center[1] + 100))
            self.screen.blit(self.mountain_image_small, (mountain_rect.topright[0] + 10, mountain_rect.topright[1]))
            self.draw_text_topleft("- Invalid move will increment your total moves by 1", self.normal_font_normal, self.red, (100, self.screen_center[1] + 150))
            self.draw_text_topleft("- Toggling your special move will count as a turn", self.normal_font_normal, self.white, (100, self.screen_center[1] + 200))
            
        # Draws the buttons
        previous_page_button = Button((100, 50), (self.screen_center[0] - 200, self.screen_center[1] + 250), "Previous", self.pixel_font_normal)
        previous_page_button.draw(self.screen)
        next_page_button = Button((100, 50), (self.screen_center[0] + 100, self.screen_center[1] + 250), "Next", self.pixel_font_normal)
        next_page_button.draw(self.screen)
        home_button = Button((100, 50), (self.screen_center[0] - 50, self.screen_center[1] + 250), "Home", self.pixel_font_normal)
        home_button.draw(self.screen)

        # Checks if the user clicked on the navigation buttons
        if previous_page_button.is_clicked() and self.first_click:
            self.current_how_to_play_page -= 1
            if self.current_how_to_play_page < 1:
                self.current_how_to_play_page = 3

        elif next_page_button.is_clicked() and self.first_click:
            self.current_how_to_play_page += 1
            if self.current_how_to_play_page > 3:
                self.current_how_to_play_page = 1

        elif home_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[1]
            self.current_how_to_play_page = 1
        
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
    

# TODO: Delete this later
# This is just for testing purposes
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

        # game_gui.screen.fill((0, 0, 100)) # Resets the screen
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