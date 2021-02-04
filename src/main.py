# import the pygame module, so you can use it
import pygame

from tile import Tile
from render import rendertile

# define a main function
width = 1600
height = 900
rows = 10
cols = 20
FPS = 60
blockwidth = width / cols
blockheight = height / rows


def translate_index(row: int, col: int):
    return row * rows + col


def addneighbours(maze: list[Tile]):
    for entity in maze:

        left = translate_index(entity.row, entity.col - 1)
        right = translate_index(entity.row, entity.col + 1)
        above = translate_index(entity.row - 1, entity.col)
        below = translate_index(entity.row + 1, entity.col)
        if left > 0:
            entity.neighbours.append(maze[left])
        if right < cols - 1:
            entity.neighbours.append(maze[right])
        if above > 0:
            entity.neighbours.append(maze[above])
        if below < rows - 1:
            entity.neighbours.append(maze[below])


def initalizemaze(numberofmazes: int, mazes: list[pygame.sprite.Group]):
    for i in range(numberofmazes):
        maze = pygame.sprite.Group()
        tiles = []
        for row in range(rows):
            for col in range(cols):
                tile = Tile(row, col, False, blockwidth, blockheight)
                maze.add(tile)
                tiles.append(tile)
        addneighbours(tiles)
        mazes.append(maze)


def main():
    pygame.init()
    pygame.display.set_caption("mazegenerator :D")

    screen = pygame.display.set_mode((width, height))
    framepersec = pygame.time.Clock()
    mazes: list[pygame.sprite.Group] = []
    initalizemaze(1, mazes)

    running = True
    currentmaze = mazes[0]
    print(len(mazes))
    print(len(mazes[0]))

    first = currentmaze.sprites().__getitem__(21)
    first.changeColor((255,0,0))
    for i in first.neighbours:
        i.changeColor((100, 100, 100))

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
