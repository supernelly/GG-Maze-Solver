import pygame, math, sys
from pygame.locals import *
from Grid import Grid
from Algorithms import *

# Resources to textures
textures = {
    0 : pygame.image.load('dirt.png'),
    1 : pygame.image.load('brick.png'),
    2 : pygame.image.load('end.png'),
    3 : pygame.image.load('guy.png'),
    4 : pygame.image.load('path.png')
}

# Select grid here
g = Grid(1)
grid = g.grid
tileSize = g.tileSize
mapWidth = g.mapWidth
mapHeight = g.mapHeight

# Display
pygame.init()
screen = pygame.display.set_mode((mapWidth * tileSize, mapHeight * tileSize))
clock = pygame.time.Clock()

# Select algorithms here
RecursiveWalk(0, 1, grid) # Start at (0, 1)   

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    for row in range(mapHeight):
        for column in range(mapWidth):
            screen.blit(textures[grid[row][column]], (column*tileSize,row*tileSize))

    pygame.display.update()