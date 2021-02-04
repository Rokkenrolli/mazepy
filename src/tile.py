import pygame

vec = pygame.math.Vector2


class Walls:
    def __init__(self):
        self.top = True
        self.right = True
        self.bottom = False
        self.left = True


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

    def changeColor(self, color: (int, int, int)):
        self.surf.fill(color)

    def set_start(self):
        self.start = True
        self.changeColor((255, 0, 0))

    def set_end(self):
        self.end = True
        self.changeColor((0, 255, 0))

    def visit(self):
        self.visited = True
        self.changeColor((0, 255, 255))
