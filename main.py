import pygame
from pygame.locals import *
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GRAY = (127, 127, 127)
BLUE = (0, 0, 255)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500


def main():
    global SCREEN
    # global CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # CLOCK = pygame.time.Clock()
    SCREEN.fill(GRAY)

    while True:
        drawGrid()
        color_rect()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    blockSize = 20  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def color_rect():
    global SCREEN
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0] // 20
    y = mouse_pos[1] // 20
    if pygame.mouse.get_pressed()[0]:
        for i in range(x, x + 1):
            for j in range(y, y + 1):
                rect = pygame.Rect(i * 20, j * 20, 20, 20)
                pygame.draw.rect(SCREEN, BLUE, rect, 0)


if __name__ == '__main__':
    main()
