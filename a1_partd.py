
from a3_maze import Maze

def find_path(the_maze, from_cell, to_cell):
    freeArr = []
    return searchPath(the_maze, from_cell, to_cell, freeArr)
    

def searchPath(the_maze, from_cell, to_cell, path):
    path.append(from_cell)

    if from_cell == to_cell:
        return path

    left = the_maze.get_left(from_cell)
    if left != -1 and left not in path:
        result = searchPath(the_maze, left, to_cell, path)
        if result:
            return result

    right = the_maze.get_right(from_cell)
    if right != -1 and right not in path:
        result = searchPath(the_maze, right, to_cell, path)
        if result:
            return result

    up = the_maze.get_up(from_cell)
    if up != -1 and up not in path:
        result = searchPath(the_maze, up, to_cell, path)
        if result:
            return result

    down = the_maze.get_down(from_cell)
    if down != -1 and down not in path:
        result = searchPath(the_maze, down, to_cell, path)
        if result:
            return result

    path.pop()

    return []











	
