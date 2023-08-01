from random import randint
import pygame

class GameSprite(pygame.sprite.Sprite):
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
        self.rotate_speed = randint(-10, 10) # The speed at which the sprite rotates
        self.screen_size = screen_size

        # The image of the sprite
        if sprite_image_path is not None:
            random_size = randint(50, 300)
            self.original_image = pygame.transform.scale(pygame.image.load(sprite_image_path).convert_alpha(), (random_size, random_size))
            self.rotated_image = pygame.transform.scale(pygame.image.load(sprite_image_path).convert_alpha(), (random_size, random_size))
            self.rect = self.original_image.get_rect()
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
            self.dx = randint(-10, 10)
            self.dy = self.dx
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
        screen.blit(self.rotated_image, self.rect)

    def rotate(self) -> None:
        '''
        Rotates the sprite.
        '''
        self.angle += self.rotate_speed
        self.rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.rotated_image.get_rect(center=self.rect.center)
