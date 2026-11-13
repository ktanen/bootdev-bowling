import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, \
BALL_STARTING_X_POS, BALL_STARTING_Y_POS, \
PIN_DECK_STARTING_X_POS, PIN_DECK_STARTING_Y_POS, \
HEADPIN_STARTING_X_POS, HEADPIN_STARTING_Y_POS

from bowlingball import BowlingBall
from bowlingpin import BowlingPin
from pindeck import PinDeck

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0.0
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    # background.fill("burlywood1")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    pins = pygame.sprite.Group()
    ball = BowlingBall(BALL_STARTING_X_POS, BALL_STARTING_Y_POS)
    pin_deck =  PinDeck(PIN_DECK_STARTING_X_POS, PIN_DECK_STARTING_Y_POS)
    pin = BowlingPin(HEADPIN_STARTING_X_POS, HEADPIN_STARTING_Y_POS)
    

    BowlingBall.containers = (updatable, drawable)
    BowlingPin.containers = (drawable, updatable)
    PinDeck.containers = (drawable)

    ball.add(drawable, updatable)
    pin_deck.add(drawable)

    screen.blit(background, (0, 0))
    pygame.display.flip()
 
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        
        screen.blit(background, (0, 0))

        screen.blit(background, ball.rect, ball.rect)

        
        pin.add(drawable, updatable, pins)

        updatable.update(dt)


        ball_mask = pygame.mask.from_surface(ball.image)
        pin_mask = pygame.mask.from_surface(pin.image)

        offset_x = pin.rect.x - ball.rect.x
        offset_y = pin.rect.y - ball.rect.y

        if ball_mask.overlap(pin_mask, (offset_x, offset_y)):
            pin.was_hit = True
            pin.velocity += ball.velocity
            
        
            

        
        


        screen.fill("burlywood1")
        for image in drawable:
            image.draw(screen) 
        
        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000

if __name__ == "__main__":
    main()
