import pygame as pg


class GUI():
    def __init__(self, screen_size: tuple, screen_title: str) -> None:
        self.screen_size_x = screen_size[0]
        self.screen_size_y = screen_size[1]
        self.screen_title = screen_title
        self.screen = pg.display.set_mode((self.screen_size_x, self.screen_size_y))
        pg.display.set_caption(self.screen_title)
        pg.display.set_icon(pg.image.load("src/Graphics/icon.png"))
        self.clock = pg.time.Clock()

        self.font = pg.font.SysFont('Arial', 30)
        self.font_small = pg.font.SysFont('Arial', 20)
        self.font_large = pg.font.SysFont('Arial', 50)
        self.font_very_large = pg.font.SysFont('Arial', 100)
        self.font_very_small = pg.font.SysFont('Arial', 15)
        self.font_very_very_small = pg.font.SysFont('Arial', 10)
        self.font_very_very_large = pg.font.SysFont('Arial', 150)

    def check_quit(self, event) -> None:
        '''
        Checks if the user has quit the game.
        
        :param event:   The event that is being checked.
        '''
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        
    def draw_text(self, text: str, font: pg.font.SysFont, colour: tuple, x: int, y: int) -> None:
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
        text_rect.center = (x, y)
        self.screen.blit(text_obj, text_rect)

if __name__ == '__main__':
    pg.init()
    game_gui = GUI((1200, 675), "Hunter vs Prey")
    is_key_pressed = False  # Flag to keep track of key press
    
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
