import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import *


def main():
    print(f"""
Starting Asteroids with pygame version: {pygame.version.ver}
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0 

    while True:
        log_state()
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

        print(dt)

   




if __name__ == "__main__":
    main()