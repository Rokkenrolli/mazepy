# import the pygame module, so you can use it
import pygame

from tile import Tile
from render import rendertile
import random

# define a main function
width = 1600
height = 900
rows = 10
cols = 20
FPS = 60
blockwidth = width / cols
blockheight = height / rows
staticlocations = True


def initalizeStartAndEnd(maze: list[Tile], static_locations=True):
    filtered = []
    if not static_locations:
        for e in maze:
            if e.row == 0 or e.row == rows - 1 or e.col == 0 or e.col == cols - 1:
                filtered.append(e)
        random.choice(filtered).set_start()
        random.choice(filtered).set_end()

    else:
        maze[0].start = True
        maze[0].changeColor((255, 0, 0))
        maze[len(maze) - 1].end = True
        maze[len(maze) - 1].changeColor((0, 255, 0))


def translate_index(row: int, col: int):
    return row * cols + col


def addneighbours(maze: list[Tile]):
    for entity in maze:

        left = translate_index(entity.row, entity.col - 1)
        right = translate_index(entity.row, entity.col + 1)
        above = translate_index(entity.row - 1, entity.col)
        below = translate_index(entity.row + 1, entity.col)
        if left > 0:
            entity.neighbours.append(maze[left])
        if right < len(maze) - 1:
            entity.neighbours.append(maze[right])
        if above > 0:
            entity.neighbours.append(maze[above])
        if below < len(maze) - 1:
            entity.neighbours.append(maze[below])


def initalizemaze(numberofmazes: int, mazes: list[list[Tile]]):
    for i in range(numberofmazes):
        maze = []
        for row in range(rows):
            for col in range(cols):
                tile = Tile(row, col, False, blockwidth, blockheight)
                maze.append(tile)
        addneighbours(maze)
        initalizeStartAndEnd(maze, static_locations=staticlocations)
        mazes.append(maze)


def main():
    pygame.init()
    pygame.display.set_caption("mazegenerator :D")

    screen = pygame.display.set_mode((width, height))
    framepersec = pygame.time.Clock()
    mazes: list[list[Tile]] = []
    initalizemaze(1, mazes)

    running = True
    currentmaze = mazes[0]
    print(len(mazes))
    print(len(mazes[0]))

    # main loopI
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        screen.fill((0, 0, 0))
        rendertile.rendermaze(screen, currentmaze)
        pygame.display.update()
        framepersec.tick(FPS)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
