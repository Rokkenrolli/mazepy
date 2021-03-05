import random

from src.generators.generators import Generator
from src.utils import translate_index
from src.tile import Tile


class Maze:

    def generate_maze(self):
        self.generator.__generate__(maze=self)
        self.finalize()

    def finalize(self):
        for cell in self.board:
            if cell.start:
                cell.set_start()
            if cell.end:
                cell.set_end()
        # TODO: other analytics here too

    def addneighbours(self, maze: list[Tile], weights):
        for entity in maze:

            left = translate_index(entity.row, entity.col - 1, self.cols)
            right = translate_index(entity.row, entity.col + 1, self.cols)
            above = translate_index(entity.row - 1, entity.col, self.cols)
            below = translate_index(entity.row + 1, entity.col, self.cols)
            if left > entity.row * self.cols - 1:
                entity.neighbours['left'] = (maze[left], weights[0])
            if right < (entity.row + 1) * self.cols:
                entity.neighbours['right'] = (maze[right], weights[1])
            if above >= 0:
                entity.neighbours['up'] = (maze[above], weights[2])
            if below < len(maze):
                entity.neighbours['down'] = (maze[below], weights[3])

    def initalizeStartAndEnd(self, maze: list[Tile], static_locations=True):
        filtered = []
        if not static_locations:
            for e in maze:
                if e.row == 0 or e.row == self.rows - 1 or e.col == 0 or e.col == self.cols - 1:
                    filtered.append(e)
            random.choice(filtered).set_start()
            random.choice(filtered).set_end()

        else:
            maze[0].set_start()
            maze[len(maze) - 1].set_end()

    def initalize(self):
        for row in range(self.rows):
            for col in range(self.cols):
                tile = Tile(row, col, False, self.blockwidth, self.blockheight)
                self.board.append(tile)
        self.addneighbours(self.board, self.weights)
        self.initalizeStartAndEnd(self.board, static_locations=self.static_locations)

    def __init__(self, rows, cols, blockwidth, blockheight, generator: Generator, weights: (float, float, float, float),
                 static_locations=True, ):
        self.rows = rows
        self.cols = cols
        self.board: list[Tile] = []
        self.blockwidth = blockwidth
        self.blockheight = blockheight
        self.static_locations = static_locations
        self.generated = False
        self.weights = weights
        self.initalize()
        self.generator = generator
