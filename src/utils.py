from enum import Enum


def translate_index(row: int, col: int, cols: int):
    return row * cols + col


def on_board(board_width: float, board_height: float, pos: (int, int)):
    return int(board_width) > pos[0] and int(board_height) > pos[1]


def generate_all(maze_collection):
    for maze in maze_collection:
        maze.generate_maze()


class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4
