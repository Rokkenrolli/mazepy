# import the pygame module, so you can use it
import pygame

from src.button import Button
from src.generators.wilson import Wilson
from src.maze import Maze
from render import render
from src.utils import generate_all, on_board

width = 1600
height = 900
scale = 0.8
number_of_mazes = 10
board_width = width * scale
board_height = height * scale
rows = 20
cols = 40
staticlocations = True
sidebar_pos_x = board_width + (width * (1 - scale) / 2)
sidebar_pos_y = height * 0.05
background_color = (0, 46, 46)
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)
board = pygame.surface.Surface((board_width, board_height))
board.fill((255, 255, 255))
screen.blit(board, (0, 0))


def initalizemazes(numberofmazes: int, mazes: list[Maze]):
    for i in range(numberofmazes):
        weights = (0.25, 0.25, 0.25, 0.25)
        maze = Maze(rows, cols, board_width / cols, board_height / rows,
                    Wilson(screen), weights=weights,
                    static_locations=staticlocations)
        mazes.append(maze)


def add_maze(mazes, weights):
    maze = Maze(rows, cols, board_width / cols, board_height / rows,
                Wilson(screen), weights=weights,
                static_locations=staticlocations)
    mazes.append(maze)


def increment(fps):
    if fps > 2000:
        return 60
    else:
        return fps + 60


def main():
    pygame.init()
    pygame.display.set_caption("maze generator :D")
    mazes: list[Maze] = []
    frames_per_sec = pygame.time.Clock()
    fps = 200
    # left right up down / cannot be zero / must add up to 1
    maze_index = 0
    initalizemazes(number_of_mazes, mazes)
    render_walls = True
    render_prev = False
    running = True
    current_maze = mazes[maze_index]
    rendering_maze = True
    add_maze_button = Button(width * 0.1, height * 0.05, (0, 0, 0),
                             (sidebar_pos_x, sidebar_pos_y + (height * 0.1)),
                             )
    print(len(mazes))
    print(len(mazes[0].board))

    # main loopI
    while running:
        screen.fill(background_color)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1 and not current_maze.generated:
                    if on_board(board_width, board_height, pos):
                        current_maze.generate_maze(rendering_maze)
                    add_maze_button.click(pos, mazes, Maze(rows, cols, board_width / cols, board_height / rows,
                                                           Wilson(screen), weights=(0.25, 0.25, 0.25, 0.25),
                                                           static_locations=staticlocations))
                if event.button == 3:
                    for tile in current_maze.board:
                        if tile.rect.collidepoint(pos):
                            tile.on_click()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    render_walls = not render_walls
                if event.key == pygame.K_w:
                    render_prev = not render_prev
                if event.key == pygame.K_RIGHT:
                    maze_index = min(maze_index + 1, len(mazes) - 1)
                    current_maze = mazes[maze_index]
                if event.key == pygame.K_LEFT:
                    maze_index = max(maze_index - 1, 0)
                    current_maze = mazes[maze_index]
                if event.key == pygame.K_e:
                    generate_all(mazes)
                if event.key == pygame.K_SPACE:
                    fps = increment(fps)
                if event.key == pygame.K_KP_ENTER:
                    rendering_maze = not rendering_maze

        if current_maze.generating:
            current_maze.update(rendering_maze)
        render.rendermaze(screen, current_maze.board, render_walls, render_prev)
        render.render_text(screen, "maze: " + str(maze_index + 1) + " / " + str(len(mazes)),
                           (board_width + (width * (1 - scale) / 2), height * 0.05), background_color, 32)
        render.render_text(screen, str(fps), (board_width + (width * (1 - scale) / 4), height * 0.01), background_color,
                           12)
        add_maze_button.draw(screen, "Add Maze")
        pygame.display.flip()
        frames_per_sec.tick(fps)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
