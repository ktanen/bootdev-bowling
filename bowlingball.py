import pygame
from circleshape import CircleShape
from constants import BALL_RADIUS, BOWLER_SPEED, BALL_SPEED, ROLL_COOLDOWN_SECONDS
from bowlingpin import BowlingPin
import math
class BowlingBall(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BALL_RADIUS)
        self.starting_position = self.position
        self.rect = pygame.Rect((self.position.x, self.position.y, BALL_RADIUS, BALL_RADIUS))
        self.roll_cooldown_timer = 0
        self.roll_initiated = False

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
        if self.roll_initiated:
            self.do_roll_update(dt)
                

        self.roll_cooldown_timer -= dt


            

    def roll(self):
        if self.roll_cooldown_timer <= 0:
            self.roll_initiated = True
            self.roll_cooldown_timer = ROLL_COOLDOWN_SECONDS

    def do_roll_update(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(180)
        scaled_vector = rotated_vector * BALL_SPEED * dt
        if self.position.y >= 0:
            self.position.y += scaled_vector.y
        else:
            self.roll_initiated = False
        

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
