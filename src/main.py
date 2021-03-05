# import the pygame module, so you can use it
import pygame

from src.generators.wilson import Wilson
from src.maze import Maze
from render import render
from src.utils import on_board

width = 1600
height = 900
board_width = width * 0.8
board_height = height * 0.8
rows = 10
cols = 20
FPS = 60
staticlocations = True
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
board = pygame.surface.Surface((board_width, board_height))
board.fill((255, 255, 255))
screen.blit(board, (0, 0))
frames_per_sec = pygame.time.Clock()


def initalizemazes(numberofmazes: int, mazes: list[Maze]):
    for i in range(numberofmazes):
        maze = Maze(rows, cols, board_width / cols, board_height / rows,
                    Wilson((0.25, 0.25, 0.25, 0.25), False, screen),
                    static_locations=staticlocations)
        mazes.append(maze)


def main():
    pygame.init()
    pygame.display.set_caption("maze generator :D")
    mazes: list[Maze] = []
    initalizemazes(1, mazes)
    render_walls = True
    render_prev = True
    running = True
    current_maze = mazes[0]

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
                if event.button == 1 and not current_maze.generated:
                    current_maze.generate_maze()
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    for tile in current_maze.board:
                        if tile.rect.collidepoint(pos):
                            tile.on_click()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    render_walls = not render_walls
                if event.key == pygame.K_w:
                    render_prev = not render_prev

        render.rendermaze(screen, current_maze.board, render_walls, render_prev)
        pygame.display.flip()
        frames_per_sec.tick(FPS)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
