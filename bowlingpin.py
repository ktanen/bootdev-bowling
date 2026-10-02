import pygame
from constants import PIN_WIDTH, PIN_HEIGHT, LINE_WIDTH

class BowlingPin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.width = PIN_WIDTH
        self.height = PIN_HEIGHT
        self.rect = pygame.Rect((self.position.x, self.position.y, self.width, self.height))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", self.rect)
        

