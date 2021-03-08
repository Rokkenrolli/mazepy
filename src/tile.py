import pygame

from src.utils import Direction

vec = pygame.math.Vector2


class Tile(pygame.sprite.Sprite):

    def __init__(self, row: int, col: int, visited: bool, width: float, height: float):
        super(Tile, self).__init__()
        self.default_color = (189, 115, 189)
        self.row = row
        self.col = col
        self.visited = visited
        self.pos = vec(col * width, row * height)
        self.surf = pygame.surface.Surface((width, height))
        self.surf.fill(self.default_color)
        self.rect = self.surf.get_rect(center=(self.pos.x + (width / 2), self.pos.y + (height / 2)))
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.neighbours = {}
        self.start = False
        self.end = False
        self.prev = None
        self.on_focus = False

    def on_click(self):
        self.on_focus = not self.on_focus
        for n in self.neighbours.values():
            if self.on_focus:
                n[0].change_color((0, 0, 255))
                if not self.start and not self.end:
                    self.change_color((255, 255, 0))
            else:
                n[0].change_color(self.default_color)
                if not self.start and not self.end:
                    self.change_color(self.default_color)

    def get_neighbours(self):
        a = []
        for n in self.neighbours.values():
            a.append(n[0])
        return a

    def neighbour_probabilities(self):
        a = []
        for n in self.neighbours.values():
            a.append(n[1])
        # map the probabilities so they always add to 1
        # keeping their proportional size
        a = list(map(lambda x: x / sum(a), a))
        return a

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
            self.walls['left'] = False
            other.walls['right'] = False
            return Direction.LEFT
        if self.row is other.row and self.col is other.col - 1:
            self.walls['right'] = False
            other.walls['left'] = False
            return Direction.RIGHT
        if self.row is other.row + 1 and self.col is other.col:
            self.walls['top'] = False
            other.walls['bottom'] = False
            return Direction.UP
        if self.row is other.row - 1 and self.col is other.col:
            self.walls['bottom'] = False
            other.walls['top'] = False
            return Direction.DOWN

    def visit(self):
        self.visited = True
        self.change_color((255, 255, 255))
        return self
