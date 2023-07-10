from random import randint
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, screen_size: tuple, sprite_image_path: str = None, sprite_position: tuple = None , sprite_move_speed: tuple = None) -> None:
        '''
        Initializes the game sprite.
        
        :param screen_size:             The size of the screen.
        :param sprite_image_path:       The path to the sprite image.
        :param sprite_position:         The position of the sprite.
        :param sprite_move_speed:       The speed of the sprite.
        '''
        super().__init__()  # Initialize the parent class

        self.angle = 0 # The angle of the 
        self.screen_size = screen_size

        # The image of the sprite
        if sprite_image_path is not None:
            self.image = pygame.transform.scale(pygame.image.load(sprite_image_path).convert_alpha(), (200, 200))
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(0, 0, 50, 50)
            self.image = pygame.Surface(self.rect.size)
            self.image.fill((255, 0, 0))  # Red
        # The position of the sprite
        if sprite_position is None:
            self.rect.x = randint(0, self.screen_size[0] - self.rect.width)
            self.rect.y = randint(0, self.screen_size[1] - self.rect.height)
        else:
            self.rect.x = sprite_position[0]
            self.rect.y = sprite_position[1]
        # The speed of the sprite
        if sprite_move_speed is None:
            self.dx = 5
            self.dy = 5
        else:
            self.dx = sprite_move_speed[0]
            self.dy = sprite_move_speed[1]

    def update(self) -> None:
        '''
        Update the sprite's position and perform any necessary logic.
        '''
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left <= 0 or self.rect.right >= self.screen_size[0]:
            self.dx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_size[1]:
            self.dy *= -1

    def draw(self, screen) -> None:
        '''
        Draws the sprite on the screen.
        
        :param screen:                  The screen that the sprite is being drawn on.
        '''
        screen.blit(self.image, self.rect)
