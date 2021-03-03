import pygame
from src.main import main
from src.tile import Tile


def renderlines(screen, tile: pygame.sprite.Sprite):
    if tile.walls['top']:
        pygame.draw.line(screen, (0, 0, 0), tile.rect.topleft, tile.rect.topright, 2)
    if tile.walls['right']:
        pygame.draw.line(screen, (0, 0, 0), tile.rect.topright, tile.rect.bottomright, 2)
    if tile.walls['left']:
        pygame.draw.line(screen, (0, 0, 0), tile.rect.topleft, tile.rect.bottomleft, 2)
    if tile.walls['bottom']:
        pygame.draw.line(screen, (0, 0, 0), tile.rect.bottomleft, tile.rect.bottomright, 2)


def rendermaze(screen: pygame.surface.Surface, maze: list[Tile]):
    for entity in maze:
        screen.blit(entity.surf, entity.rect)
        renderlines(screen, entity)
