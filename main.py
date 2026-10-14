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
    # background.fill("burlywood1")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    removable = pygame.sprite.Group()
    pins = pygame.sprite.Group()
    ball = BowlingBall(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.1)

    pin = BowlingPin(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 5)
    
    BowlingBall.containers = (updatable, drawable)
    BowlingPin.containers = (drawable, removable)

    ball.add(drawable, updatable)
    pin.add(drawable, removable, pins)

    screen.blit(background, (0, 0))
    pygame.display.flip()
 
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        
        screen.blit(background, (0, 0))

        screen.blit(background, ball.rect, ball.rect)

            
        
        updatable.update(dt)


        ball_mask = pygame.mask.from_surface(ball.image)
        pin_mask = pygame.mask.from_surface(pin.image)

        offset_x = pin.rect.x - ball.rect.x
        offset_y = pin.rect.y - ball.rect.y

        if ball_mask.overlap(pin_mask, (offset_x, offset_y)):
            print("Collision detected")
            
     
        


        screen.fill("burlywood1")
        for image in drawable:
            image.draw(screen) 
        
        pygame.display.flip()
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000

if __name__ == "__main__":
    main()
