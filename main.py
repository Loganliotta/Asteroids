import pygame
import constants
from logger import log_state
from player import Player


def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        clock.tick(60) 
        dt = clock.get_time() / 1000.0
        player.draw(screen)
        player.update(dt)


        pygame.display.flip()



if __name__ == "__main__":
    main()
