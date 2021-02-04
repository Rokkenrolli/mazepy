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

    def changeColor(self, color: (int, int, int)):
        self.surf.fill(color)
