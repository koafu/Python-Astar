import pygame 
import random
from node import Node
from astar import * 

def show_node(window, x, y, color, margin):
    '''Draws node in grid'''
    window.fill(color, rect=[(x*c) + margin, (y*c) + margin, c - margin, c - margin])

white = (255,255,255)
black = (0,0,0)
red =  (255,0,0)
green = (0,255,0)
blue = (44, 130, 230)
yellow = (252,223,3)

pygame.init()

width = 800
height = 800

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('A* Algorithm')
clock = pygame.time.Clock()
window.fill(white)

grid_size = 50
grid = [[] for n in range(grid_size)]
for y in range(grid_size):
    for x in range(grid_size):
        grid[y].append(Node(x,y))

for y in grid:
    for node in y:
        node.addNeighbours(grid)

start = grid[0][0]
start.wall = False
end = grid[grid_size-1][grid_size-1]
end.wall = False

running = True
c = width / grid_size       

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    
    x,y = 0,0
    margin = 1
    for cols in grid:
        pygame.draw.line(window, black, (x,0), (x,height), margin)
        for rows in cols:
            pygame.draw.line(window, black, (0,y), (width,y), margin)
        x += c
        y += c

    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x].wall:
                show_node(window, x, y, black, margin)

    if astar(grid, start, end) == 'failure':
        print(astar(grid, start, end))
    else:
        for node in astar(grid, start, end):
            show_node(window, node.x, node.y, blue, margin)

    pygame.display.update()
    clock.tick(60)
