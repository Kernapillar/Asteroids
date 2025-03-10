import pygame
from constants import *
from player import Player

def main(): 
    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)



    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updateable.update(dt)
        
        for object in drawable: 
            object.draw(screen)

        pygame.display.flip()
        tick_val = clock.tick(60)
        dt = tick_val / 1000




if __name__ == "__main__":
    main()