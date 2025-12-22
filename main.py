import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    print(f"""
Starting Asteroids with pygame version: {pygame.version.ver}
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
""")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    

    dt = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.position.distance_to(player.position) <= player.radius + asteroid.radius:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.position.distance_to(shot.position) <= asteroid.radius + shot.radius:
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill() 


        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        

   




if __name__ == "__main__":
    main()