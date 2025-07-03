import pygame

from common.game_default import GameDefault
from model.board.board import Board
from view.board_view import BoardView

if __name__ == "__main__":
    pygame.init()

    board = Board(id=1)
    print(board.)

    # Set screen dimensions based on board size and cell pixel size
    screen_width = board.column_count() * GameDefault.CELL_PX
    screen_height = board.row_count() * GameDefault.CELL_PX
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Board Display")

    clock = pygame.time.Clock()
    view = BoardView(board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))  # Clear screen with a dark background
        view.draw_board(screen)         # Draw the board and pieces
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
