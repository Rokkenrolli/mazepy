import numpy as np
import pygame

from src.generators.generators import Generator
from src.tile import Tile


class HitItself(Exception):
    pass


class Wilson(Generator):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.cell: Tile = None
        self.path = []

    def step(self, cell, unvisited, path):
        neighbor_cell: Tile
        cell.change_color((115, 141, 189))
        neighbor_cell = np.random.choice(cell.get_neighbours(), p=cell.neighbour_probabilities())
        if neighbor_cell in unvisited:
            raise HitItself
        else:
            path.append(neighbor_cell)
        cell.change_color(cell.default_color)
        return neighbor_cell

    def wilson_walk(self, unvisited):

        self.cell = np.random.choice(unvisited)
        self.path: [Tile] = [self.cell]
        while self.cell in unvisited:
            self.cell = self.step(self.cell, unvisited, self.path)
            for c in self.path:
                c.change_color((255, 0, 0))
        prev = None
        for c in self.path:
            default = (255, 255, 255)
            c.default_color = default
            c.visit()
            if prev:
                prev.prev = c
                prev.break_wall(c)
                unvisited.remove(prev)
                # print("row", prev.row, "col", prev.col)
                # print("row", prev.prev.row, "col", prev.prev.col)
                # print("-------------")
            prev = c
        return unvisited

    def __update__(self, maze):

        if len(maze.unvisited) > 0:
            # print(unvisited)
            # print(len(maze.unvisited))
            try:
                maze.unvisited = self.wilson_walk(maze.unvisited)
                return True
            except HitItself:
                return True
        return False
