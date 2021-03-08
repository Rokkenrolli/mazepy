import pygame

from src.render.render import render_text


class Button:
    def __init__(self, width, height, colour, pos, ):  # And other customisation options
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.colour = colour


    def draw(self, screen, text):
        screen.blit(self.image, self.rect)
        render_text(screen, text, self.rect.center, self.colour, 32)



    def click(self, pos,mazes,maze):
        if self.rect.collidepoint(pos):
            mazes.append(maze)


