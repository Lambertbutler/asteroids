import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    started, failed = pygame.init()

    print(f"started pygame modules: {started}")
    print(f"failed to start: {failed}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        if color:
            screen.fill("black")
            color = not color
        else:
            screen.fill("white")
            color = not color
        
        
        pygame.display.flip()



if __name__ == "__main__":
    main()