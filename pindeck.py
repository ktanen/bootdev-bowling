import pygame
import math
from bowlingpin import BowlingPin
from circleshape import CircleShape
from constants import LINE_WIDTH, PIN_DECK_RADIUS
class PinDeck(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PIN_DECK_RADIUS)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 
        LINE_WIDTH)


    def triangle(self, margin=0.0):
        forward = pygame.Vector2(0, 1)          # apex toward the bowler
        r = self.radius + 2 * margin            # inradius = r / 2
        right = pygame.Vector2(1, 0) * (r * math.sqrt(3) / 2)
        a = self.position + forward * r
        b = self.position - forward * (r / 2) - right
        c = self.position - forward * (r / 2) + right
        return [a, b, c]