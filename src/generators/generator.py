import random
import numpy as np

from src.tile import Tile


def generator(maze: list[Tile], weights: (int, int, int, int), use_weights: bool):
    unvisited = []
    for tile in maze:
        tile.walls.top[1] = weights[0]
        tile.walls.right[1] = weights[1]
        tile.walls.bottom[1] = weights[2]
        tile.walls.left[1] = weights[3]
        unvisited.append(tile)

    first = np.random.choice(unvisited)
    first.visited = True
    unvisited.remove(first)

    while len(unvisited) > 0:
        #print(unvisited)
        #print(len(unvisited))
        cell = np.random.choice(unvisited)
        path = [cell]

        while cell in unvisited:
            neighbor_cell: Tile
            if (use_weights):
                weights_array = []
                # TODO: add weigths to this
            else:
                neighbor_cell = np.random.choice(cell.neighbours)
                if neighbor_cell in path:
                    path = path[0:path.index(neighbor_cell) + 1]
                else:
                    path.append(neighbor_cell)

                cell = neighbor_cell
        prev = None
        for cell in path:
            if prev:
                prev.prev = cell
                prev.break_wall(cell)
                unvisited.remove(prev)
            prev = cell
