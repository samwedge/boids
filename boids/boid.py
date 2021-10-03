import numpy as np
from p5 import Vector


class Boid():
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.position = Vector(x, y)
        self.velocity = Vector(*((np.random.rand(2) - 0.5) * 10))
        self.acceleration = Vector(*((np.random.rand(2) - 0.5) / 2))
        self.max_speed = 5
        self.perception = 100
        self.max_force = 0.1

    def update(self, boids):
        self._apply_behaviour(boids)
        self.position += self.velocity
        self.velocity += self.acceleration
        if np.linalg.norm(self.velocity) > self.max_speed:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * self.max_speed

        self.acceleration = Vector(*np.zeros(2))

    def _apply_behaviour(self, boids):
        alignment = self._align(boids)
        cohesion = self._cohesion(boids)
        separation = self._separation(boids)
        self.acceleration += alignment + cohesion + separation

    def _align(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vec = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < self.perception:
                avg_vec += boid.velocity
                total += 1
        if total > 0:
            avg_vec /= total
            avg_vec = Vector(*avg_vec)
            avg_vec = (avg_vec / np.linalg.norm(avg_vec)) * self.max_speed
            steering = avg_vec - self.velocity

        return steering

    def _cohesion(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        center_of_mass = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < self.perception:
                center_of_mass += boid.position
                total += 1
        if total > 0:
            center_of_mass /= total
            center_of_mass = Vector(*center_of_mass)
            vec_to_com = center_of_mass - self.position
            if np.linalg.norm(vec_to_com) > 0:
                vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * self.max_speed
            steering = vec_to_com - self.velocity
            if np.linalg.norm(steering) > self.max_force:
                steering = (steering / np.linalg.norm(steering)) * self.max_force

        return steering

    def _separation(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vector = Vector(*np.zeros(2))
        for boid in boids:
            distance = np.linalg.norm(boid.position - self.position)
            if self.position != boid.position and distance < self.perception:
                diff = self.position - boid.position
                diff /= distance
                avg_vector += diff
                total += 1
        if total > 0:
            avg_vector /= total
            avg_vector = Vector(*avg_vector)
            if np.linalg.norm(steering) > 0:
                avg_vector = (avg_vector / np.linalg.norm(steering)) * self.max_speed
            steering = avg_vector - self.velocity
            if np.linalg.norm(steering)> self.max_force:
                steering = (steering /np.linalg.norm(steering)) * self.max_force

        return steering
