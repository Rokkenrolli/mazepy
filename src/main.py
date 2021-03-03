# import the pygame module, so you can use it
import pygame

from src.generators.wilson import Wilson
from src.maze import Maze
from render import rendertile

width = 1600
height = 900
rows = 10
cols = 20
FPS = 60
staticlocations = True


def initalizemazes(numberofmazes: int, mazes: list[Maze]):
    for i in range(numberofmazes):
        maze = Maze(rows, cols, width / cols, height / rows, Wilson((0.25,0.25,0.25,0.25), False), static_locations=staticlocations)
        mazes.append(maze)


def main():
    pygame.init()
    pygame.display.set_caption("mazegenerator :D")


    screen = pygame.display.set_mode((width, height))
    framepersec = pygame.time.Clock()
    mazes: list[Maze] = []
    initalizemazes(1, mazes)

    running = True
    currentmaze = mazes[0]

    print(len(mazes))
    print(len(mazes[0].board))

    # main loopI
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not currentmaze.generated:
                    currentmaze.generate_maze()
        screen.fill((0, 0, 0))
        rendertile.rendermaze(screen, currentmaze.board)
        pygame.display.update()
        framepersec.tick(FPS)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
