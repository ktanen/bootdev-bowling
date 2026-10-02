import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from bowlingball import BowlingBall
from bowlingpin import BowlingPin

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    BowlingBall.containers = (updatable, drawable)
    BowlingPin.containers = (drawable)

    ball = BowlingBall(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.1)
    pin = BowlingPin(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        updatable.update(dt)
        
        screen.fill("burlywood1")

        for image in drawable:
            image.draw(screen)

        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000

if __name__ == "__main__":
    main()
