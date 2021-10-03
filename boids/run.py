from p5 import size, background, run

from boids.world import World


world = World(width=1000, height=1000, flock_size=25)


def setup():
    size(world.width, world.height)


def draw():
    background(30, 30, 47)
    world.update()
    world.draw()


if __name__ == '__main__':
    run()
