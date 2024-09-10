from constants import *
from circleshape import *
import pygame
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y, radius)
    
    def split(self):
        # if the radius is the smallest it can be remove itself else split
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            # create 2 small asteroids, and speed them up
            random_angle = uniform(20,50)
            a1_velocity = self.velocity.rotate(random_angle)
            a2_velocity = self.velocity.rotate(-random_angle)
            newradius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x,self.position.y,newradius)
            a2 = Asteroid(self.position.x,self.position.y,newradius)
            a1.velocity = a1_velocity * 1.2
            a2.velocity = a2_velocity * 1.2
            self.kill()
            
            
    
       
    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, width=2) 

    def update(self,dt):
        self.position += self.velocity * dt