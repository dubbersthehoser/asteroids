import random

import pygame

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,  (255, 255, 255), self.position ,self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        degree = random.uniform(20, 50)

        a1 = self.velocity.rotate(degree)
        a2 = self.velocity.rotate(-degree)

        nr = self.radius - ASTEROID_MIN_RADIUS

        na1 = Asteroid(self.position.x, self.position.y, nr)
        na2 = Asteroid(self.position.x, self.position.y, nr)

        na1.velocity = a1 * 1.2
        na2.velocity = a2 * 1.2
        self.kill()
