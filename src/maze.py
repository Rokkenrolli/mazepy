import random

from src.utils import translate_index
from src.tile import Tile


class Maze:

    def addneighbours(self, maze: list[Tile]):
        for entity in maze:

            left = translate_index(entity.row, entity.col - 1, self.cols)
            right = translate_index(entity.row, entity.col + 1, self.cols)
            above = translate_index(entity.row - 1, entity.col, self.cols)
            below = translate_index(entity.row + 1, entity.col, self.cols)
            if left > 0:
                entity.neighbours.append(maze[left])
            if right < len(maze) - 1:
                entity.neighbours.append(maze[right])
            if above > 0:
                entity.neighbours.append(maze[above])
            if below < len(maze) - 1:
                entity.neighbours.append(maze[below])

    def initalizeStartAndEnd(self, maze: list[Tile], static_locations=True):
        filtered = []
        if not static_locations:
            for e in maze:
                if e.row == 0 or e.row == self.rows - 1 or e.col == 0 or e.col == self.cols - 1:
                    filtered.append(e)
            random.choice(filtered).set_start()
            random.choice(filtered).set_end()

        else:
            maze[0].start = True
            maze[0].changeColor((255, 0, 0))
            maze[len(maze) - 1].end = True
            maze[len(maze) - 1].changeColor((0, 255, 0))

    def initalize(self):
        for row in range(self.rows):
            for col in range(self.cols):
                tile = Tile(row, col, False, self.blockwidth, self.blockheight)
                self.board.append(tile)
        self.addneighbours(self.board)
        self.initalizeStartAndEnd(self.board, static_locations=self.static_locations)

    def __init__(self, rows, cols, blockwidth, blockheight, static_locations=True):
        self.rows = rows
        self.cols = cols
        self.board: list[Tile] = []
        self.blockwidth = blockwidth
        self.blockheight = blockheight
        self.static_locations = static_locations
        self.generating = False
        self.initalize()
