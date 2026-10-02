import pygame
from circleshape import CircleShape
from constants import BALL_RADIUS, LINE_WIDTH, BOWLER_SPEED

class BowlingBall(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_RADIUS)
        self.rect = pygame.Rect((self.position.x, self.position.y, BALL_RADIUS, BALL_RADIUS))
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius)
        
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(-90)
        player_with_speed_vector = rotated_vector * BOWLER_SPEED * dt
        self.position += player_with_speed_vector
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.move(dt)

        if keys[pygame.K_LEFT]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.roll()   

    def roll(self):
        """Implement this once the left and right movement works"""
        pass
