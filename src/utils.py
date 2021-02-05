from enum import Enum


def translate_index(row: int, col: int, cols: int):
    return row * cols + col


class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

