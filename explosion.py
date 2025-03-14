import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, EXPLOSION_RADIUS

class Explosion(CircleShape): 
    def __init__(self, x, y):
        super().__init__(x, y, EXPLOSION_RADIUS)
        self.duration = 0.5
    
    def draw(self, screen): 
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt): 
        # self.position += self.velocity * dt
        self.duration -= dt
        if self.duration <= 0: 
            self.kill()
    
    def explode(self, dt, screen): 
        if self.radius == self.explosion_radius: 
            return
        pygame.draw.circle(screen, "red", self.position, self.explosion_radius, 2)