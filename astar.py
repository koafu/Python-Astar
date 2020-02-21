import pygame
from node import Node

class Astar():

    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end

    def recontstruct_path(self, current):
        '''
        finds path to end node
        '''
        total_path = []
        end = current
        temp = current
        while temp.cameFrom:
            total_path.insert(0,temp.cameFrom)
            temp = temp.cameFrom
        total_path.append(end)
        return total_path


    def astar(self):
        '''
        astar algorithm
        '''
        self.start.g = 0
        self.start.f = self.start.heuristic(self.end)
        open_set = [self.start]
        closed_set = []

        while len(open_set) != 0:
            current = min(open_set, key=lambda x:x.f)

            if current == self.end:
                return self.recontstruct_path(current)
                
            open_set.remove(current)
            closed_set.append(current)
            for neighbour in current.neighbours:

                if neighbour in closed_set or neighbour.wall == True:
                    continue

                tentative_g = current.g + 1
                if neighbour in open_set:
                    if tentative_g < neighbour.g:
                        neighbour.g = tentative_g
                        neighbour.cameFrom = current
                        neighbour.f = neighbour.g + neighbour.heuristic(self.end)

                else:
                    neighbour.g = tentative_g
                    open_set.append(neighbour)
                    neighbour.f = neighbour.g + neighbour.heuristic(self.end)
                    neighbour.cameFrom = current

        return 'failure'