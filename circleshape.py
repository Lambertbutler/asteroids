import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def wraparound(self):
        # if we go off the right side of the screen
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        # if we go off the bottom of the screen
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius        
    
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
    
    def collision(self,other):
        combinedRad = self.radius + other.radius
        distanceTo = self.position.distance_to(other.position)
        return combinedRad > distanceTo