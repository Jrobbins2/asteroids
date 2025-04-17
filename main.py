import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    py_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_time = pygame.time.Clock()
    dt = 0
    the_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    the_player.draw(py_display)
    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        py_display.fill((0,0,0))
        the_player.draw(py_display)
        pygame.display.flip()
        dt = py_time.tick(60)/1000

if __name__ == "__main__":
    main()