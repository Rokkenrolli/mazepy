import pygame

from src.utils import Direction

vec = pygame.math.Vector2


class Walls:
    def __init__(self):
        self.top = [True, 0.25]
        self.right = [True, 0.25]
        self.bottom = [False, 0.25]
        self.left = [True, 0.25]


class Tile(pygame.sprite.Sprite):

    def __init__(self, row: int, col: int, visited: bool, width: float, height: float):
        super(Tile, self).__init__()
        self.row = row
        self.col = col
        self.visited = visited
        self.pos = vec(col * width, row * height)
        self.surf = pygame.surface.Surface((width, height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(self.pos.x + (width / 2), self.pos.y + (height / 2)))
        self.walls = Walls()
        self.neighbours = []
        self.start = False
        self.end = False
        self.prev = None

    def change_color(self, color: (int, int, int)):
        self.surf.fill(color)

    def set_start(self):
        self.start = True
        self.change_color((255, 0, 0))

    def set_end(self):
        self.end = True
        self.change_color((0, 255, 0))

    def visit(self):
        self.visited = True
        self.change_color((0, 255, 255))

    # determines which direction the other block is to this block and breaks it
    def break_wall(self, other):
        if self.row is other.row and self.col is other.col + 1:
            self.walls.left[0] = False
            other.walls.right[0] = False
            return Direction.LEFT
        if self.row is other.row and self.col is other.col - 1:
            self.walls.right[0] = False
            other.walls.left[0] = False
            return Direction.RIGHT
        if self.row is other.row + 1 and self.col is other.col:
            self.walls.top[0] = False
            other.walls.bottom[0] = False
            return Direction.UP
        if self.row is other.row - 1 and self.col is other.col:
            self.walls.bottom[0] = False
            other.walls.top[0] = False
            return Direction.DOWN




