from constants import *
from circleshape import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y, radius)
    
    def split(self):
        self.kill()
    
       
    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, width=2) 

    def update(self,dt):
        self.position += self.velocity * dt