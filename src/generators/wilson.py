import numpy as np
import pygame

from src.generators.generators import Generator
from src.tile import Tile


class HitItself(Exception):
    pass


class Wilson(Generator):

    def __init__(self, weights: (int, int, int, int), use_weights: bool, screen):
        super().__init__()
        self.weights = weights
        self.use_weights = use_weights
        self.screen = screen

    def step(self, cell, unvisited, path):
        neighbor_cell: Tile
        cell.change_color((115, 141, 189))
        if self.use_weights:
            weights_array = []
            # TODO: add weights to this
        else:
            neighbor_cell = np.random.choice(list(cell.neighbours.values()))
            if neighbor_cell in unvisited:
                raise HitItself
            else:
                path.append(neighbor_cell)

            return neighbor_cell

    def wilson_walk(self, unvisited):
        temp = unvisited.copy()
        cell = np.random.choice(temp)
        path = [cell]
        while cell in temp:
            cell = self.step(cell, temp, path)
        prev = None
        for c in path:
            default = (255, 255, 255)
            c.default_color = default
            c.change_color(default)
            if prev:
                prev.prev = c
                prev.break_wall(c)
                temp.remove(prev)
                print("row", prev.row, "col", prev.col)
                print("row", prev.prev.row, "col", prev.prev.col)
                print("-------------")
            prev = c
        return temp

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
            try:
                unvisited = self.wilson_walk(unvisited)
            except HitItself:
                continue
