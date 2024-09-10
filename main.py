import pygame
from constants import *
from Player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField
from shot import Shot

def main():

    pygame.init()

    # create drawable groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shotsFired = pygame.sprite.Group()
    # Auto Add new objects groups
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shotsFired, updatable, drawable)

    # Create objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    AsteroidField()
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
            
        # check for colisions
        for asteroid in asteroids:
            # check collsion with play
            if asteroid.collision(player):
                print("Game over!")
                return
            
            # check colision with shot
            for shot in shotsFired:
                if shot.collision(asteroid):
                    #remove the shot from all groups
                    shot.kill()
                    asteroid.split()

            
            
                
        # draw all objects to screen
        for obj in drawable:
            obj.draw(screen)
        
        # update screen 
        pygame.display.flip()

        # wait 1/60sec limit screen update rate
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()