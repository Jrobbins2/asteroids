from constants import *
import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        the_angle = random.uniform(20, 50)
        split1 = self.velocity.rotate(the_angle)
        split2 = self.velocity.rotate((the_angle * -1))
        new_size = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_size)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_size)
        asteroid1.velocity = split1 * 1.2
        asteroid2.velocity = split2 * 1.2