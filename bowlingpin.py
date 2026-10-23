import pygame
import math
from constants import PIN_WIDTH, PIN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT


class BowlingPin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.starting_position = self.position
        self.width = PIN_WIDTH
        self.height = PIN_HEIGHT
        self.rect = pygame.Rect((self.position.x, self.position.y, self.width, self.height))
        self.image = pygame.surface.Surface((self.width, self.height))
        self.was_hit = False
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", self.rect)

    def update(self, dt):
        if self.was_hit:
            self.pin_update(dt)        
            
    def pin_update(self, dt):
        unit_vector = pygame.Vector2(0,1)
        
        angled_vector = unit_vector.rotate(self.velocity.angle_to(pygame.Vector2(0, 180)))
        speed = self.velocity.magnitude()
        scaled_vector: pygame.Vector2 = angled_vector * speed * dt

        if (PIN_HEIGHT + self.position.y >= 0):
            self.position += scaled_vector
           # self.rect.topleft = (int(self.position.x), int(self.position.y))
            self.rect.move_ip(scaled_vector)
        else:
            self.was_hit = False
            self.position.update(self.starting_position)
            self.rect.topleft = (int(self.starting_position.x), int(self.starting_position.y)) #self.position
            self.rect.clamp_ip(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 5), PIN_WIDTH, PIN_HEIGHT)
            self.position = pygame.Vector2(self.rect.topleft)
            self.velocity = pygame.Vector2(0, 0)

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)