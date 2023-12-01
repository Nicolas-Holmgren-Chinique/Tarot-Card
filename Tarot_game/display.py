import pygame
import os
# from pygame.locals import *

# creates the display/background


# def main():
pygame.init()
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("Taroter")
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Sets the frames per seconds to 60 which later gets used.
FPS = 60

# everything to do with the design and visuals of game


def draw_window():
    while True:
        win.fill((0, 204, 122))
        win.blit(450, 250)
        pygame.display.update()
    # print("Welcome to Taroter!")


# Checks if the player quit the game
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
