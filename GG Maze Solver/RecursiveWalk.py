import pygame, math, sys
from pygame.locals import *

#resources to textures
textures = {
    0 : pygame.image.load('dirt.png'),
    1 : pygame.image.load('brick.png'),
    2 : pygame.image.load('end.png'),
    3 : pygame.image.load('guy.png'),
}

#Tilemap
grid = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 1]]

def search(x, y):
    if grid[x][y] == 2:
        print('found at %d,%d' % (x, y))
        return True
    elif grid[x][y] == 1:
        print('wall at %d,%d' % (x, y))
        return False
    elif grid[x][y] == 3:
        print('visited at %d,%d' % (x, y))
        return False
    
    print('visiting %d,%d' % (x, y))

    # mark as visited
    grid[x][y] = 3

    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True

    return False
    
#display
tileSize = 40
mapWidth = 10
mapHeight = 10
pygame.init()
screen = pygame.display.set_mode((mapWidth*tileSize, mapHeight*tileSize))
clock = pygame.time.Clock()
    
search(0, 1) # start at (0, 0)   

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