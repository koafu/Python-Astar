import pygame
from node import Node
from astar import Astar

class Grid():
    
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 1000
        pygame.display.set_caption("A* pathfinding")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

        self.grid_size = 100
        self.grid = [[] for n in range(self.grid_size)]

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                self.grid[y].append(Node(x,y))
        for y in self.grid:
            for node in y:
                node.addNeighbours(self.grid)

        self.margin = 1

        self.start = self.grid[0][0]
        self.start.wall = False
        self.end = self.grid[self.grid_size-1][self.grid_size-1]
        self.end.wall = False
        self.node_size = self.width / self.grid_size

    def show_node(self, screen, color, x, y, margin):
        screen.fill(color, rect=[(x*self.node_size) + margin, (y*self.node_size) + margin, self.node_size - margin, self.node_size - margin])


    def draw_grid(self, screen, grid, grid_size, margin):
        screen.fill((255,255,255))
        x,y = 0,0
        for cols in grid:
            pygame.draw.line(screen, (0,0,0), (x,0), (x,self.height), margin)
            for rows in cols:
                pygame.draw.line(screen, (0,0,0), (0,y), (self.width,y), margin)
            x += self.node_size
            y += self.node_size

        for y in range(grid_size):
            for x in range(grid_size):
                if grid[y][x].wall:
                    self.show_node(screen, (0,0,0), x, y, margin)

    def run(self):

        while not self.exit:
    
            self.screen.fill((255,255,255))            
            self.draw_grid(self.screen, self.grid, self.grid_size, self.margin)
            algorithm = Astar(self.grid, self.start, self.end)
            path = algorithm.astar()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            
            if path == 'failure':
                print('failure')
            else:
                for path_node in path:
                    self.show_node(self.screen, (52, 158, 235), path_node.x, path_node.y, self.margin)

            pygame.display.flip()
            self.clock.tick(self.ticks)

        pygame.quit()


if __name__ == '__main__':
    algo_grid = Grid()
    algo_grid.run()
