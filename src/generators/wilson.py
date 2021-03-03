import random
import numpy as np

from src.generators.generators import Generator
from src.tile import Tile


class Wilson(Generator):

    def __init__(self, weights: (int, int, int, int), use_weights: bool, ):
        self.weights = weights
        self.use_weights = use_weights

    def __generate__(self, maze):
        maze.generated = True
        unvisited = []
        for tile in maze.board:
            unvisited.append(tile)

        first = np.random.choice(unvisited)
        unvisited.remove(first)

        while len(unvisited) > 0:
            # print(unvisited)
            # print(len(unvisited))
            cell = np.random.choice(unvisited)
            path = [cell]

            while cell in unvisited:
                neighbor_cell: Tile
                if self.use_weights:
                    weights_array = []
                    # TODO: add weights to this
                else:
                    neighbor_cell = np.random.choice(list(cell.neighbours.values()))
                    if neighbor_cell in path:
                        path = path[0:path.index(neighbor_cell) + 1]
                    else:
                        path.append(neighbor_cell)

                    cell = neighbor_cell
            prev = None
            for c in path:
                if prev:
                    prev.prev = c
                    prev.break_wall(c)
                    unvisited.remove(prev)
                prev = c

