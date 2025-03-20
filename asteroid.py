import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape): 
    def __init__(self, x, y, radius, update_score_callback=None):
        super().__init__(x, y, radius)
        self.update_score = update_score_callback 
    
    def draw(self, screen): 
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt): 
        self.position += self.velocity * dt

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            if self.update_score: 
                self.update_score(10)
            return
        new_angle = random.uniform(20, 50)
        child1 = self.velocity.rotate(new_angle)
        child2 = self.velocity.rotate(-new_angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, child_radius, self.update_score)
        asteroid1.velocity = child1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, child_radius, self.update_score)
        asteroid2.velocity = child2 * 1.2
        