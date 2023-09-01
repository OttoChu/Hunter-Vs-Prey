import pygame

from Button import Button
from GameSprite import GameSprite
from Hunter import Hunter
from Tiles import *


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

        # States
        self.all_states = ["welcome_page", "homepage", "how_to_play_page", "setting_page", "difficulty_page", 
                           "fog_of_war_page", "ability_page", "game_page", "choose_teleport_page", "game_over_page"]
        self.current_state = self.all_states[0] # The current state of the game

        # Fonts
        self.pixel_font_very_small = pygame.font.Font("src/Fonts/Tickerbit-italic.otf", 15)
        self.pixel_font_small = pygame.font.Font("src/Fonts/Tickerbit-italic.otf", 20)
        self.pixel_font_normal = pygame.font.Font("src/Fonts/Tickerbit-italic.otf", 30)
        self.pixel_font_large = pygame.font.Font("src/Fonts/Tickerbit-italic.otf", 50)
        self.pixel_font_very_large = pygame.font.Font("src/Fonts/Tickerbit-italic.otf", 75)
        self.pixel_font_huge = pygame.font.Font("src/Fonts/Tickerbit-italic.otf", 100)

        # Colours
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        # Graphics
        self.background_image = pygame.transform.scale(pygame.image.load("src/Graphics/background.png"), self.screen_size)
        self.hunter_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/hunter.png"), (30, 30))
        self.hunter_image_medium = pygame.transform.scale(pygame.image.load("src/Graphics/hunter.png"), (50, 50))
        self.prey_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/prey.png"), (30, 30))
        self.prey_image_medium = pygame.transform.scale(pygame.image.load("src/Graphics/prey.png"), (50, 50))
        self.tree_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/tree.png"), (30, 30))
        self.tree_image_medium = pygame.transform.scale(pygame.image.load("src/Graphics/tree.png"), (50, 50))
        self.mountain_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/mountain.png"), (30, 30))
        self.mountain_image_medium = pygame.transform.scale(pygame.image.load("src/Graphics/mountain.png"), (50, 50))
        self.fog_image_small = pygame.transform.scale(pygame.image.load("src/Graphics/fog.png"), (30, 30))
        self.fog_image_medium = pygame.transform.scale(pygame.image.load("src/Graphics/fog.png"), (50, 50))
        self.arrow_image = pygame.transform.scale(pygame.image.load("src/Graphics/arrow.png"), (50, 50))
        
        # Sprites
        game_over_sprite_path = "src/Graphics/funny_cat.png"
        self.game_over_sprite_list = [GameSprite(self.screen_size, game_over_sprite_path) for i in range(20)] # The game over sprite

        # Input variables
        self.first_keypress = False # Flag to keep track of whether the current key press is the first time
        self.first_click = False # Flag to keep track of whether the current mouse press is the first time

        # Random
        self.game_version = "v2.0.0"
        self.running = True # Flag to keep track of whether the game is running or not
        self.wait_counter = 0 # Counter used to keep track of how long the frames has passed
        self.current_how_to_play_page = 1 # The current page of the how to play section
        self.current_ability_page = 1 # The current page of the ability section
        
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
    
    def draw_text_bottomright(self, text: str, font: pygame.font.Font, colour: tuple, bottomright_position: tuple) -> pygame.Rect:
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
        text_rect.bottomright = bottomright_position
        self.screen.blit(text_obj, text_rect)
        return text_rect
    
    def draw_game_version(self) -> None:
        '''
        Draws the game version on the screen.
        '''
        self.draw_text_bottomright(self.game_version, self.pixel_font_very_small, self.white, (self.screen_size[0] - 5, self.screen_size[1] - 5))
    
    def draw_line(self, start_position: tuple, end_position: tuple, colour: tuple, width: int) -> None:
        '''
        Draws a line on the screen.

        :param start_position:  The starting position of the line.
        :param end_position:    The ending position of the line.
        :param colour:          The colour of the line.
        :param width:           The width of the line.
        '''
        pygame.draw.line(self.screen, colour, start_position, end_position, width)

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
        self.draw_text_center("Press any key to continue"+ '.' * dot_counter, self.pixel_font_normal, (255, 255, 255), (self.screen_center[0], self.screen_center[1] + 100))
        
        # Checks if the user has pressed any key
        if self.first_keypress or self.first_click:
            self.current_state = self.all_states[1]
            self.wait_counter = 0
            
    def homepage(self) -> bool:
        '''
        Draws the homepage of the game.

        :return:    True if the user has pressed the play button, False otherwise.
        '''
        self.draw_text_center("Hunter Vs Prey!", self.pixel_font_huge, self.white, (self.screen_center[0], self.screen_center[1] - 200))
        new_game_button = Button((300, 150), (self.screen_center[0] - 150, self.screen_center[1] - 25), "Play", self.pixel_font_very_large)
        new_game_button.draw(self.screen)
        how_to_play_button = Button((200, 100), (self.screen_center[0] - 375, self.screen_center[1] + 150), "How to play", self.pixel_font_normal)
        how_to_play_button.draw(self.screen)
        settings_button = Button((200, 100), (self.screen_center[0] - 100, self.screen_center[1] + 150), "Settings", self.pixel_font_normal)
        settings_button.draw(self.screen)
        quit_button = Button((200, 100), (self.screen_center[0] + 175, self.screen_center[1] + 150), "Quit", self.pixel_font_normal)
        quit_button.draw(self.screen)

        # Checks if the user has pressed any key
        if new_game_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[7]
            return True
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
        self.draw_text_center("How to play", self.pixel_font_very_large, self.white, (self.screen_center[0], self.screen_center[1] - 250))
        if self.current_how_to_play_page == 1: # Page 1
            self.draw_text_topleft("Goal", self.pixel_font_large, self.white, (100, self.screen_center[1] - 150))
            self.draw_text_topleft("- Hunter Vs Prey is a game where you play as a hunter and you have to", self.pixel_font_normal, self.white, (100, self.screen_center[1] - 100))
            self.draw_text_topleft("  catch the prey", self.pixel_font_normal, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- The prey is controlled by an AI and will try to run away from you", self.pixel_font_normal, self.white, (100, self.screen_center[1]))
            self.draw_text_topleft("- The game will end when the Hunter is on the same tile as the Prey", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.draw_text_center("Good luck!", self.pixel_font_large, self.green, (self.screen_center[0], self.screen_center[1] + 150))

        elif self.current_how_to_play_page == 2: # Page 2
            self.draw_text_topleft("Controls", self.pixel_font_large, self.white, (100, self.screen_center[1] - 150))
            self.draw_text_topleft("- Press 'WASD'  or arrow keys to move", self.pixel_font_normal, self.white, (100, self.screen_center[1] - 100))
            self.draw_text_topleft("- Press 'E' or right shift to use ability", self.pixel_font_normal, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- You may also use the on-screen buttons to move and use ability", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 50))
        
        elif self.current_how_to_play_page == 3: # Page 3
            self.draw_text_topleft("Rules", self.pixel_font_large, self.white, (100, self.screen_center[1] - 150))
            prey_rect = self.draw_text_topleft("- The Prey is represented as", self.pixel_font_normal, self.white, (100, self.screen_center[1] - 100))
            self.screen.blit(self.prey_image_small, (prey_rect.topright[0] + 10, prey_rect.topright[1]))
            hunter_rect = self.draw_text_topleft("and the Hunter is represented as", self.pixel_font_normal, self.white, (prey_rect.topright[0] + 50, prey_rect.topright[1]))
            self.screen.blit(self.hunter_image_small, (hunter_rect.topright[0] + 10, hunter_rect.topright[1]))
            fog_rect = self.draw_text_topleft("- Fog are represented as", self.pixel_font_normal, self.white, (100, self.screen_center[1] - 50))
            self.screen.blit(self.fog_image_small, (fog_rect.topright[0] + 10, fog_rect.topright[1]))
            self.draw_text_topleft("- All animals can move 1 tile in any direction per turn", self.pixel_font_normal, self.white, (100, self.screen_center[1]))
            tree_rect = self.draw_text_topleft("- The squares that you can be on are represented as", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.screen.blit(self.tree_image_small, (tree_rect.topright[0] + 10, tree_rect.topright[1]))
            mountain_rect = self.draw_text_topleft("- The squares that you can NOT be on are represented as", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 100))
            self.screen.blit(self.mountain_image_small, (mountain_rect.topright[0] + 10, mountain_rect.topright[1]))
            self.draw_text_topleft("- Invalid move will increment your total moves by 1", self.pixel_font_normal, self.red, (100, self.screen_center[1] + 150))
            
        # Draws the page number
        self.draw_text_topleft(f"Page {self.current_how_to_play_page} of 3", self.pixel_font_small, self.white, (100, self.screen_center[1] + 265))
        
        # Draws the navigation buttons
        previous_page_button = Button((100, 50), (self.screen_center[0] - 200, self.screen_center[1] + 250), "Previous", self.pixel_font_small)
        previous_page_button.draw(self.screen)
        next_page_button = Button((100, 50), (self.screen_center[0] + 100, self.screen_center[1] + 250), "Next", self.pixel_font_small)
        next_page_button.draw(self.screen)
        home_button = Button((100, 50), (self.screen_center[0] - 50, self.screen_center[1] + 250), "Home", self.pixel_font_small)
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
        self.draw_text_center("Settings", self.pixel_font_very_large, self.white, (self.screen_center[0], self.screen_center[1] - 250))
        self.draw_text_center("You may change all game settings by pressing the buttons below", self.pixel_font_normal, self.white, (self.screen_center[0], self.screen_center[1] - 150))
        difficulty_button = Button((200, 100), (self.screen_center[0] - 375, self.screen_center[1] - 50), "Difficulty", self.pixel_font_normal)
        difficulty_button.draw(self.screen)
        fog_of_war_button = Button((200, 100), (self.screen_center[0] - 100, self.screen_center[1] - 50), "Fog of War", self.pixel_font_normal)
        fog_of_war_button.draw(self.screen)
        ability_button = Button((200, 100), (self.screen_center[0] + 175, self.screen_center[1] - 50), "Ability", self.pixel_font_normal)
        ability_button.draw(self.screen)
        home_button = Button((100, 50), (self.screen_center[0] - 50, self.screen_center[1] + 250), "Home", self.pixel_font_small)
        home_button.draw(self.screen)

        # Checks if the user clicked on the buttons
        if home_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[1]
        elif difficulty_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[4]
        elif fog_of_war_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[5]
        elif ability_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[6]

    def difficulty(self, difficulty_name: str) -> int:
        '''
        Draws the difficulty page of the game.

        :param chosen_difficulty: The current difficulty of the game.

        :return: The new difficulty of the game.
        '''
        self.draw_text_center("Difficulty", self.pixel_font_very_large, self.white, (self.screen_center[0], self.screen_center[1] - 250))
        self.draw_text_center("You may change the difficulty of the game by pressing the buttons below", self.pixel_font_normal, self.white, (self.screen_center[0], self.screen_center[1] - 150))
        self.draw_text_center(f"Current Difficulty: {difficulty_name}", self.pixel_font_normal, self.white, (self.screen_center[0], self.screen_center[1] - 100))
        
        # Draws the buttons
        extra_easy_button = Button((200, 100), (self.screen_center[0] - 375, self.screen_center[1] - 50), "Extra Easy", self.pixel_font_normal)
        extra_easy_button.draw(self.screen)
        easy_button = Button((200, 100), (self.screen_center[0] - 100, self.screen_center[1] - 50), "Easy", self.pixel_font_normal)
        easy_button.draw(self.screen)
        medium_button = Button((200, 100), (self.screen_center[0] + 175, self.screen_center[1] - 50), "Normal", self.pixel_font_normal)
        medium_button.draw(self.screen)
        hard_button = Button((200, 100), (self.screen_center[0] - 375, self.screen_center[1] + 100), "Hard", self.pixel_font_normal)
        hard_button.draw(self.screen)
        extra_hard_button = Button((200, 100), (self.screen_center[0] - 100, self.screen_center[1] + 100), "Extra Hard", self.pixel_font_normal)
        extra_hard_button.draw(self.screen)
        impossible_button = Button((200, 100), (self.screen_center[0] + 175, self.screen_center[1] + 100), "Impossible", self.pixel_font_normal)
        impossible_button.draw(self.screen)

        # Draws the navigation buttons
        home_button = Button((100, 50), (self.screen_center[0] + 50, self.screen_center[1] + 250), "Home", self.pixel_font_small)
        home_button.draw(self.screen)
        back_button = Button((100, 50), (self.screen_center[0] - 150, self.screen_center[1] + 250), "Back", self.pixel_font_small)
        back_button.draw(self.screen)

        # Checks if the user clicked on the buttons
        if home_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[1]
        elif back_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[3]
        elif extra_easy_button.is_clicked() and self.first_click:
            return 1
        elif easy_button.is_clicked() and self.first_click:
            return 2
        elif medium_button.is_clicked() and self.first_click:
            return 3
        elif hard_button.is_clicked() and self.first_click:
            return 4
        elif extra_hard_button.is_clicked() and self.first_click:
            return 5
        elif impossible_button.is_clicked() and self.first_click:
            return 6

    def fog_of_war(self, status: bool) -> None:
        '''
        Draws the fog of war page of the game.

        :param status: The current status of the fog of war.
        '''
        self.draw_text_center("Fog of War", self.pixel_font_very_large, self.white, (self.screen_center[0], self.screen_center[1] - 250))
        self.draw_text_center("Increase the difficultly by limiting your vision of the map!", self.pixel_font_normal, self.white, (self.screen_center[0], self.screen_center[1] - 150))
        self.draw_text_center(f"Current Fog of War: {'ON' if status else 'OFF'}", self.pixel_font_normal, self.white, (self.screen_center[0], self.screen_center[1] - 100))
        self.draw_text_center("The Spotter ability is unavailable if Fog of War is off ", self.pixel_font_normal, self.red, (self.screen_center[0], self.screen_center[1] + 150))
        self.draw_text_center("The Jumper ability will be chosen instead", self.pixel_font_normal, self.red, (self.screen_center[0], self.screen_center[1] + 180))

        # Draws the buttons
        on_button = Button((200, 100), (self.screen_center[0] -250, self.screen_center[1] - 25), "On", self.pixel_font_large)
        on_button.draw(self.screen)
        off_button = Button((200, 100), (self.screen_center[0] + 50, self.screen_center[1] - 25), "Off", self.pixel_font_large)
        off_button.draw(self.screen)

        # Draws the navigation buttons
        home_button = Button((100, 50), (self.screen_center[0] + 50, self.screen_center[1] + 250), "Home", self.pixel_font_small)
        home_button.draw(self.screen)
        back_button = Button((100, 50), (self.screen_center[0] - 150, self.screen_center[1] + 250), "Back", self.pixel_font_small)
        back_button.draw(self.screen)

        # Checks if the user clicked on the buttons
        if home_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[1]
        elif back_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[3]
        elif on_button.is_clicked() and self.first_click:
            return True
        elif off_button.is_clicked() and self.first_click:
            return False
    
    def ability(self, ability_name: str) -> None:
        '''
        Draws the ability page of the game.
        '''
        self.draw_text_center("Ability", self.pixel_font_very_large, self.white, (self.screen_center[0], self.screen_center[1] - 250))
        self.draw_text_center("Change your in-game ability to have a different experience", self.pixel_font_normal, self.white, (self.screen_center[0], self.screen_center[1] - 150))
        self.draw_text_center(f"Current Ability: {ability_name}", self.pixel_font_normal, self.white, (self.screen_center[0], self.screen_center[1] - 100))

        if self.current_ability_page == 1: # Jumper
            self.draw_text_topleft("Jumper", self.pixel_font_large, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- Moves 2 tiles in the same direction in one turn", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.draw_text_topleft("- Can jump over mountains", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 100))
            self.draw_text_topleft("- 10 charges per game", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 150))

        elif self.current_ability_page == 2: # Time Stopper
            self.draw_text_topleft("Time Stopper", self.pixel_font_large, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- Makes 3 moves in one turn", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.draw_text_topleft("- The Prey will not move when this ability is used", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 100))
            self.draw_text_topleft("- 5 charge per game", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 150))
        
        elif self.current_ability_page == 3: # Teleporter
            self.draw_text_topleft("Teleporter", self.pixel_font_large, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- Teleports to a different tile on the map", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.draw_text_topleft("- The teleportation range is the 9x9 tiles around the Hunter", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 100))
            tree_rect = self.draw_text_topleft(f"- You can only teleport to a", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 150))
            self.screen.blit(self.tree_image_small, (tree_rect.topright[0] + 10, tree_rect.topright[1]))
            self.draw_text_topleft(f"- 1 charge per game", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 200))
        elif self.current_ability_page == 4: # Spotter
            self.draw_text_topleft("Spotter", self.pixel_font_large, self.white, (100, self.screen_center[1] - 50))
            self.draw_text_topleft("- Reveals the 11x11 tiles around the Hunter", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 50))
            self.draw_text_topleft("- Choosing this ability will turn Fog of War ON", self.pixel_font_normal, self.red, (100, self.screen_center[1] + 100))
            self.draw_text_topleft("- 3 charges per game", self.pixel_font_normal, self.white, (100, self.screen_center[1] + 150))

        # Draws the page number
        self.draw_text_center(f"Page {self.current_ability_page} of 4", self.pixel_font_small, self.white, (100, self.screen_center[1] + 265))

        # Draws the buttons
        select_ability_button = Button((200, 100), (self.screen_size[0] - 300, self.screen_center[1] - 80), "Select", self.pixel_font_large)
        select_ability_button.draw(self.screen)

        # Draws the navigation buttons
        previous_page_button = Button((100, 50), (self.screen_center[0] + 25, self.screen_center[1] - 55), "Previous", self.pixel_font_small)
        previous_page_button.draw(self.screen)
        next_page_button = Button((100, 50), (self.screen_center[0] + 150, self.screen_center[1] - 55), "Next", self.pixel_font_small)
        next_page_button.draw(self.screen)

        # Draws the home and back buttons
        home_button = Button((100, 50), (self.screen_center[0] + 50, self.screen_center[1] + 250), "Home", self.pixel_font_small)
        home_button.draw(self.screen)
        back_button = Button((100, 50), (self.screen_center[0] - 150, self.screen_center[1] + 250), "Back", self.pixel_font_small)
        back_button.draw(self.screen)

        # Checks if the user clicked on the buttons
        if home_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[1]
            self.current_ability_page = 1
        elif back_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[3]
            self.current_ability_page = 1
        elif previous_page_button.is_clicked() and self.first_click:
            self.current_ability_page -= 1
            if self.current_ability_page < 1:
                self.current_ability_page = 4
        elif next_page_button.is_clicked() and self.first_click:
            self.current_ability_page += 1
            if self.current_ability_page > 4:
                self.current_ability_page = 1
        elif select_ability_button.is_clicked() and self.first_click:
            return self.current_ability_page

    def game(self, game_map: list, fog: bool, turn_num: int, hunter: Hunter) -> str:
        '''
        Draws the game page of the game.

        :param game_map:        The map of the game
        :param fog:             Whether or not to draw the fog of war
        :param turn_num:        The current turn number
        :param hunter:          The hunter object

        :return:                The player's choice
        '''
        # Draw the game map
        hunter_position = hunter.get_position()
        for row in range(len(game_map)):
            for col in range(len(game_map[row])):
                position = (40*col + 550, 40*row + 40)
                change = False
                if fog:
                    if (col < (hunter_position[0] - hunter.visibility) or col > (hunter_position[0] + hunter.visibility) 
                        or row < (hunter_position[1] - hunter.visibility) or row > (hunter_position[1] + hunter.visibility)):
                        change = True
                if change:
                    self.screen.blit(self.fog_image_small, position)
                elif game_map[row][col] == T:
                    self.screen.blit(self.tree_image_small, position)
                elif game_map[row][col] == H:
                    self.screen.blit(self.hunter_image_small, position)
                elif game_map[row][col] == P:
                    self.screen.blit(self.prey_image_small, position)
                elif game_map[row][col] == M:
                    self.screen.blit(self.mountain_image_small, position)

        # Draws the turn details
        self.draw_text_topleft("Make A Move", self.pixel_font_large, self.white, (50, 50))
        self.draw_text_topleft(f"Turn  {turn_num}", self.pixel_font_normal, self.white, (50, 150))
        self.draw_text_topleft(f"{hunter.moves_on_turn} move(s) left on this turn", self.pixel_font_normal, self.white, (50, 200))
        self.draw_text_topleft("Current Ability:", self.pixel_font_small, self.white, (50, 275))
        self.draw_text_topleft(f"{hunter.special_ability}", self.pixel_font_small, self.white, (250, 275))
        self.draw_text_topleft("Ability status:", self.pixel_font_small, self.white, (50, 300))
        self.draw_text_topleft(f"{'ON' if hunter.special_status else 'OFF'}", self.pixel_font_small, self.white, (250, 300))
        self.draw_text_topleft("Charges:", self.pixel_font_small, self.white, (50, 325))
        self.draw_text_topleft(f"{hunter.charges}", self.pixel_font_small, self.white, (250, 325))
              
        # Draws the buttons
        up_button = Button((100, 100), (200 , 375), '', self.pixel_font_small)
        up_button.draw(self.screen)
        self.screen.blit(self.arrow_image, (225, 400))
        down_button = Button((100, 100), (200, 485), '', self.pixel_font_small)
        down_button.draw(self.screen)
        self.screen.blit(pygame.transform.rotate(self.arrow_image, 180), (225, 510))
        left_button = Button((100, 100), (90, 485), '', self.pixel_font_small)
        left_button.draw(self.screen)
        self.screen.blit(pygame.transform.rotate(self.arrow_image, 90), (115, 510))
        right_button = Button((100, 100), (310, 485), '', self.pixel_font_small)
        right_button.draw(self.screen)
        self.screen.blit(pygame.transform.rotate(self.arrow_image, 270), (335, 510))
        ability_button = Button((320, 50), (90, 595), "Ability", self.pixel_font_normal)
        ability_button.draw(self.screen)

        # Checks if the user clicked on the buttons
        if ((up_button.is_clicked() and self.first_click)
            or ((pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]) and self.first_keypress)):
            return 'W'
        elif ((down_button.is_clicked() and self.first_click)
              or ((pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]) and self.first_keypress)):
            return 'S'
        elif ((left_button.is_clicked() and self.first_click)
              or ((pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]) and self.first_keypress)):
            return 'A'
        elif ((right_button.is_clicked() and self.first_click) 
              or ((pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]) and self.first_keypress)):
            return 'D'
        elif ((ability_button.is_clicked() and self.first_click) 
              or ((pygame.key.get_pressed()[pygame.K_e] or pygame.key.get_pressed()[pygame.K_RSHIFT]) and self.first_keypress)):
            return 'E'
        
    def choose_teleport(self, game_map: list, hunter_position: tuple, fog: bool) -> tuple:
        '''
        Draws the choose teleport page of the game.

        :param game_map:        The map of the game
        :param hunter_position: The position of the hunter
        :param fog:             Whether or not the fog of war is on

        :return:                The new position of the hunter
        '''
        # Get the teleport map
        teleport_map = []
        hunter_x, hunter_y = hunter_position
        for y in range(hunter_y - 4, hunter_y + 5):
            line = []
            if 0 < y < len(game_map):
                for x in range(hunter_x - 4, hunter_x + 5):
                    if 0 < x < len(game_map):
                        line.append(game_map[y][x])
                    else:
                        line.append(M)
            else:
                for _ in range(9):
                    line.append(M)
            teleport_map.append(line)

        # Adds the fog of war
        if fog:
            for row_num in range(len(teleport_map)):
                if row_num < 2 or row_num > 6:
                    teleport_map[row_num] = [F for _ in range(9)]
                for col_num in range(len(teleport_map[row_num])):
                    if col_num < 2 or col_num > 6:
                        teleport_map[row_num][col_num] = F

        # Draws the teleport instructions
        self.draw_text_topleft("Choose a teleport location", self.pixel_font_large, self.white, (50, 30))
        self.draw_text_topleft("Click on a tile to select a location.", self.pixel_font_small, self.white, (50, 100))
        self.draw_text_topleft("Only Tree tiles are valid locations.", self.pixel_font_small, self.white, (50, 125))
        self.draw_text_topleft("Anything else will be invalid!", self.pixel_font_small, self.red, (50, 150))
        self.draw_text_topleft("Pressing the 'Cancel' button will still use up a charge!", self.pixel_font_small, self.white, (50, 175))

        # Draws the cancel button
        cancel_button = Button((200, 100), (200, 300), "Cancel", self.pixel_font_normal)
        cancel_button.draw(self.screen)
        if cancel_button.is_clicked() and self.first_click:
            return (hunter_x, hunter_y, False)
        
        # Draws the teleport map
        x_pos, y_pos = 605, 105
        for each_row in teleport_map:
            for each_tile in each_row:
                if each_tile == T:
                    self.screen.blit(self.tree_image_medium, (x_pos, y_pos))
                elif each_tile == M:
                    self.screen.blit(self.mountain_image_medium, (x_pos, y_pos))
                elif each_tile == H:
                    self.screen.blit(self.hunter_image_medium, (x_pos, y_pos))
                elif each_tile == P:
                    self.screen.blit(self.prey_image_medium, (x_pos, y_pos))
                elif each_tile == F:
                    self.screen.blit(self.fog_image_medium, (x_pos, y_pos))
                x_pos += 60
            y_pos += 60
            x_pos = 605

        # Get the rects for the rows and columns to know which tile is chosen
        rows = []
        columns = []
        for offset in range(9):
            rows.append(pygame.Rect(600, 100 + offset*60, 540, 60))
            columns.append(pygame.Rect(600 + offset*60, 100, 60, 540))
        
        # Get the chosen tile and draw the highlight
        mouse_pos = pygame.mouse.get_pos()
        chosen_tile = [-1, -1]
        for row_num, each_row in enumerate(rows):
            if each_row.collidepoint(mouse_pos):
                chosen_tile[1] = row_num
        for column_num, each_column in enumerate(columns):
            if each_column.collidepoint(mouse_pos):
                chosen_tile[0] = column_num
        if chosen_tile != [-1, -1]:
            pygame.draw.rect(self.screen, self.red, pygame.Rect(600 + chosen_tile[0]*60, 100 + chosen_tile[1]*60, 60, 60), 2)
            if self.first_click:
                if teleport_map[chosen_tile[1]][chosen_tile[0]] == T:
                    return (hunter_x-4 + chosen_tile[0], hunter_y-4 + chosen_tile[1], True)
                return (hunter_x, hunter_y, False)
            
    def game_over(self, moves: int) -> bool:
        '''
        Draws the game over page of the game.

        :param moves: The number of moves the player made.

        :return:      True if the player wants to play again, False otherwise.
        '''
        # Draws the bouncing sprite in the background
        for each_sprite in self.game_over_sprite_list:
            each_sprite.update()
            each_sprite.rotate()
            each_sprite.draw(self.screen)
        
        # Draws the game over text
        self.draw_text_center("Game Over!", self.pixel_font_huge, self.red, (self.screen_center[0], self.screen_center[1] - 100))
        self.draw_text_center("The hunter has caught the prey!", self.pixel_font_normal, self.white, self.screen_center)
        self.draw_text_center(f"You caught the prey in {moves} moves.", self.pixel_font_large, self.green, (self.screen_center[0], self.screen_center[1] + 75))
        
        # Draws the navigation buttons
        again_button = Button((200, 100), (self.screen_center[0] - 250, self.screen_center[1] + 150), "Again", self.pixel_font_large)
        again_button.draw(self.screen)
        home_button = Button((200, 100), (self.screen_center[0] + 50, self.screen_center[1] + 150), "Home", self.pixel_font_large)
        home_button.draw(self.screen)

        # Checks if the user clicked on the buttons
        if again_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[7]
            return True
        elif home_button.is_clicked() and self.first_click:
            self.current_state = self.all_states[1]
            return False