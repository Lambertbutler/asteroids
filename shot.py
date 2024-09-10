import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        self.ttl = 5
        self.alive = 0
    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, width=2) 

    def timeToLive(self):
        if self.ttl <= self.alive:
            self.kill()
    
    def update(self,dt):
        self.wraparound()
        self.timeToLive()
        self.alive += dt
        self.position += self.velocity * dt   