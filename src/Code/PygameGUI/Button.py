import pygame

class Button():
    '''
    The Button class is used to create a button.
    '''
    def __init__(self, size: tuple, position: tuple, text: str, font: pygame.font.Font, 
                 text_colour: tuple = None, normal_colour: tuple = None, highlight_colour: tuple = None) -> None:
        '''
        Initializes the button.
        
        :param size:                The size of the button.
        :param position:            The position of the button.
        :param text:                The text of the button.
        :param font:                The font of the button.
        :param text_colour:         The colour of the text of the button.
        :param normal_colour:       The colour of the button when it is not being hovered over.
        :param highlight_colour:    The colour of the button when it is being hovered over.
        '''
        self.size = size
        self.position = position
        self.text = text
        self.font = font
        self.text_colour = (0, 0, 0) if text_colour is None else text_colour
        self.normal_colour = (0, 255, 255) if normal_colour is None else normal_colour
        self.highlight_colour = (0, 255, 0) if highlight_colour is None else highlight_colour


    def draw(self, screen: pygame.Surface) -> None:
        '''
        Draws the button on the screen.
        
        :param screen:              The screen that the button is being drawn on.
        '''
        if self.is_hovering():
            pygame.draw.rect(screen, self.highlight_colour, (self.position[0], self.position[1], self.size[0], self.size[1]))
        else:
            pygame.draw.rect(screen, self.normal_colour, (self.position[0], self.position[1], self.size[0], self.size[1]))
            
        text_obj = self.font.render(self.text, True, self.text_colour)
        text_rect = text_obj.get_rect()
        text_rect.center = (self.position[0] + (self.size[0] // 2), self.position[1] + (self.size[1] // 2))
        screen.blit(text_obj, text_rect)

    def is_hovering(self) -> bool:
        '''
        Checks if the mouse is hovering over the button.
        
        :return:                   True if the mouse is hovering over the button, False otherwise.
        '''
        mouse_position = pygame.mouse.get_pos()
        if (self.position[0] <= mouse_position[0] <= self.position[0] + self.size[0] 
            and self.position[1] <= mouse_position[1] <= self.position[1] + self.size[1]):
            return True
        return False
    
    def is_clicked(self) -> bool:
        '''
        Checks if the mouse is clicking the button.
        
        :return:                    True if the mouse is clicking the button, False otherwise.
        '''
        return self.is_hovering() and pygame.mouse.get_pressed()[0]