import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from bomb import Bomb
from explosion import Explosion

def main(): 
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    Bomb.containers = (updateable, drawable, bombs)
    Explosion.containers = (updateable, drawable, explosions)

    clock = pygame.time.Clock()
    dt = 0

    score = 0

    def update_score(num = 0):  
        nonlocal score, text
        score += num
        text = font.render(f"Score: {score}", True, "White")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField(update_score)

    font = pygame.font.Font(None, 32)
    text = font.render(f"Score: {score}", True, "White")
    text_rectangle = text.get_rect()
    text_rectangle.center = (100, SCREEN_HEIGHT - 50)



    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        screen.blit(text, text_rectangle)


        updateable.update(dt)

        for asteroid in asteroids: 
            if player.detect_collision(asteroid):
                print(f"Game over! Final Score: {score}")
                sys.exit()

        for explosion in explosions: 
            if player.detect_collision(explosion):
                print(f"Game over! Final Score: {score}")
                sys.exit()

        for asteroid in asteroids: 
            for shot in shots: 
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids: 
            for bomb in bombs: 
                if asteroid.detect_collision(bomb):
                    bomb.explode()

        for asteroid in asteroids: 
            for explosion in explosions: 
                if asteroid.detect_collision(explosion):
                    asteroid.split()
            


        for object in drawable: 
            object.draw(screen)

        pygame.display.flip()
        tick_val = clock.tick(60)
        dt = tick_val / 1000




if __name__ == "__main__":
    main()