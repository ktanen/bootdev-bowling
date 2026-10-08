import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SPEED
from bowlingball import BowlingBall
from bowlingpin import BowlingPin

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0.0
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("burlywood1")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    ball = BowlingBall(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.1)
    pin = BowlingPin(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ballsprite = pygame.sprite.RenderPlain(ball)
    BowlingBall.containers = (updatable, drawable)
    BowlingPin.containers = (drawable)
    screen.blit(background, (0, 0))
    pygame.display.flip()
 
    while True:
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        
        screen.blit(background, (0, 0))

        

            
        
        ballsprite.update(dt)

        
        ball.draw(screen)


                
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
