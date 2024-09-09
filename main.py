import pygame
from constants import *
from Player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    started, failed = pygame.init()

    print(f"started pygame modules: {started}")
    print(f"failed to start: {failed}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0
    color = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill screen with black
        screen.fill("black")

        # update all objects
        for obj in updatable:
            obj.update(dt)

        # draw all objects to screen
        for obj in drawable:
            obj.draw(screen)
        
        # update screen 
        pygame.display.flip()

        # wait 1/60sec limit screen update rate
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()