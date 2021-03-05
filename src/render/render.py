import pygame
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


def rendermaze(screen: pygame.surface.Surface, maze: list[Tile], render_walls:bool, render_prev: bool):
    for entity in maze:
        screen.blit(entity.surf, entity.rect)
        if render_walls:
            renderlines(screen, entity)
        if render_prev:
            renderprev(screen, entity)


def renderprev(screen: pygame.surface.Surface, tile: pygame.sprite.Sprite):
    if tile.prev:
        pygame.draw.line(screen, (0, 250, 0), tile.rect.center, tile.prev.rect.center, 2)
