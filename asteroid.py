import pygame
from circleshape import CircleShape

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def draw(self): 
        pygame.draw.circle(self.position, self.radius, 2)

    def update(self, dt): 
        self.position += self.velocity * dt