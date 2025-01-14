import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    drawables = pygame.sprite.Group()
    updateables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (drawables, updateables)
    Shot.containers = (drawables, updateables, shots)
    Asteroid.containers = (drawables, updateables, asteroids)
    AsteroidField.containers = (updateables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable in updateables:
            updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.dose_cross(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.dose_cross(player):
                print("Game over!")
                return
        screen.fill((0,0,0))
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
