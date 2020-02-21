import random

class Node():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cameFrom = None
        self.wall = False
        self.g = None
        self.f = None
        self.neighbours = []

        if random.uniform(0,1) < 0.3:
            self.wall = True

    def heuristic(self, end):
        '''
        calculates shortest distance between self and end node 
        '''
        dstX = abs(end.x - self.x)
        dstY = abs(end.y - self.y)
        if dstY > dstX:
            distance = 14 * dstX + 10 * (dstY - dstX)
        else:
            distance = 14 * dstY + 10 * (dstX - dstY)
        return distance

    def addNeighbours(self, grid):
        '''
        adds all wakable neighbours of self to a list 
        '''
        if self.x < len(grid[0]) - 1:                            # right
            self.neighbours.append(grid[self.y][self.x + 1])
        if self.x > 0:                                           # left
            self.neighbours.append(grid[self.y][self.x - 1])
        if self.y > 0:                                           # up
            self.neighbours.append(grid[self.y - 1][self.x])
        if self.y < len(grid) - 1:                               # down
            self.neighbours.append(grid[self.y + 1][self.x])

        if self.x < len(grid[0]) - 1 and self.y > 0:             # right up
            self.neighbours.append(grid[self.y - 1][self.x + 1])
        if self.x < len(grid[0]) - 1 and self.y < len(grid) - 1: # right down
            self.neighbours.append(grid[self.y + 1][self.x + 1])
        if self.x > 0 and self.y > 0:                            # left up
            self.neighbours.append(grid[self.y - 1][self.x - 1])
        if self.x > 0 and self.y < len(grid) - 1:                # left down
            self.neighbours.append(grid[self.y + 1][self.x - 1])
