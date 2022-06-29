from tracemalloc import start
from turtle import st
import pygame
from pygame.locals import *
import sys

# program description : find the shortest path between two points with obstacles between them using A* algorithm

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

Started = 0
Ended = 0

startingSquare = [0, 0]
endingSquare = [0, 0]
obstacles = [[0, 0]]


def main():
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(GRAY)
    pygame.display.set_caption("Pathfinder")

    # choose starting square, then choose ending square, then ask for obstacles
    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if Started == 0:
                    print("Choose starting square")
                    chooseStartingSquare()
                    print(startingSquare)
                elif Ended == 0:
                    print("Choose ending square")
                    chooseEndingSquare()
                    print(endingSquare)
                else:
                    print("Choose obstacles")
                    while True:
                        drawObstacle()
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == MOUSEBUTTONDOWN:
                                if pygame.mouse.get_pressed()[0]:
                                    drawObstacle()
                                    print(obstacles)
                                else:
                                    break
                        pygame.display.update()
        pygame.display.update()


def drawGrid():
    blockSize = 20  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def chooseStartingSquare():
    global SCREEN
    global Started
    global startingSquare
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0] // 20
    y = mouse_pos[1] // 20
    if pygame.mouse.get_pressed()[0]:
        rect = pygame.Rect(x * 20, y * 20, 20, 20)
        pygame.draw.rect(SCREEN, BLUE, rect, 0)
        Started = 1
        startingSquare = [x, y]
    pygame.display.update()


def chooseEndingSquare():
    global SCREEN
    global Ended
    global endingSquare
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0] // 20
    y = mouse_pos[1] // 20
    if pygame.mouse.get_pressed()[0]:
        rect = pygame.Rect(x * 20, y * 20, 20, 20)
        pygame.draw.rect(SCREEN, RED, rect, 0)
        Ended = 1
        endingSquare = [x, y]
    pygame.display.update()


def drawObstacle():
    global SCREEN
    global obstacles
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0] // 20
    y = mouse_pos[1] // 20
    if pygame.mouse.get_pressed()[0]:
        rect = pygame.Rect(x * 20, y * 20, 20, 20)
        pygame.draw.rect(SCREEN, BLACK, rect, 0)
        obstacles.append([x, y])


if __name__ == '__main__':
    main()
