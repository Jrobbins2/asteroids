import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    py_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    the_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ast_field = AsteroidField()
    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        py_display.fill((0,0,0))
        for i in updatable:
            i.update(dt)
        for i in asteroids:
            if i.collisions(the_player):
                print("Game over!")
                raise SystemExit()
            for ii in shots:
                if i.collisions(ii):
                    i.split()
                    ii.kill()
        for i in drawable:
            i.draw(py_display)
        pygame.display.flip()
        dt = py_time.tick(60)/1000

if __name__ == "__main__":
    main()