import numpy as np
from p5 import stroke, circle

from boids.boid import Boid


class World:
    def __init__(self, width, height, flock_size):
        self.width = width
        self.height = height
        self.flock = [Boid(*np.random.rand(2)*1000, width, height) for _ in range(flock_size)]

    def update(self):
        for boid in self.flock:
            boid.update(self.flock)

        self._keep_boids_on_map()

    def draw(self):
        for boid in self.flock:
            stroke(255)
            circle(boid.position.x, boid.position.y, 10)

    def _keep_boids_on_map(self):
        for boid in self.flock:
            if boid.position.x > self.width:
                boid.position.x = 0
            elif boid.position.x < 0:
                boid.position.x = self.width

            if boid.position.y > self.height:
                boid.position.y = 0
            elif boid.position.y < 0:
                boid.position.y = self.height


