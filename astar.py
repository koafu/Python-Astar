from node import Node

def recontstruct_path(current):
    total_path = []
    end = current
    temp = current
    while temp.cameFrom:
        total_path.insert(0,temp.cameFrom)
        temp = temp.cameFrom
    total_path.append(end)
    return total_path


def astar(grid, start, goal):
    
    start.g = 0
    start.f = start.heuristic(goal)
    open_set = [start]
    closed_set = []

    while len(open_set) != 0:
        current = min(open_set, key=lambda x:x.f)

        if current == goal:
            print("DONE")
            return recontstruct_path(current)
            
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
                    neighbour.f = neighbour.g + neighbour.heuristic(goal)

            else:
                neighbour.g = tentative_g
                open_set.append(neighbour)
                neighbour.f = neighbour.g + neighbour.heuristic(goal)
                neighbour.cameFrom = current

    return 'failure'

