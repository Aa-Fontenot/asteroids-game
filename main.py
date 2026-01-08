import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot
import sys

highscores_list = []
def main():
    print(f"""
Starting Asteroids with pygame version: {pygame.version.ver}
""")

    pygame.init()
    screen = pygame.display.set_mode((1920,1080), flags=pygame.FULLSCREEN|pygame.SCALED)

    default_font = pygame.font.Font("./Hyperspace.ttf", 52)

    
    

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

    current_score = 0 
    
    def highscores_list_str_to_int_list(highscore_file):
        




    

    dt = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        log_state()
        screen.fill("black")

        try:
            with open("./highscores.txt", "x") as file:
                pass
        except FileExistsError:
            pass

        with open("./highscores.txt", "r") as file:
            highscores_list = file.read()
            if len(highscores_list) == 0:
                highest_score = 0
            else:
                highest_score = max(highscores_list)
                    

            
            

            
        score = default_font.render(f"Score: {current_score}", True, (255, 255, 255))
        highscore = default_font.render(f"Highscore: {highest_score}", True, (255, 255, 255))
        screen.blit(score, (0,0))
        screen.blit(highscore, (0, 52))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.position.distance_to(player.position) <= player.radius + asteroid.radius:
                log_event("player_hit")
                print(f"Game Over!\nYour score was {current_score}")
                with open("./highscores.txt", "a") as file:
                    file.write(f"'{current_score}'\n")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.position.distance_to(shot.position) <= asteroid.radius + shot.radius:
                    log_event("asteroid_shot")
                    if asteroid.radius == ASTEROID_MAX_RADIUS:
                        current_score += 1
                    elif ASTEROID_MIN_RADIUS < asteroid.radius < ASTEROID_MAX_RADIUS:
                        current_score += 2
                    elif asteroid.radius == ASTEROID_MIN_RADIUS:
                        current_score += 3 
                    asteroid.split()
                    shot.kill() 
        



        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        



if __name__ == "__main__":
    main()