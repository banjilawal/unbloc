from typing import Tuple

import pygame
from pygame import Color

from common.game_default import GameDefault
from model.board.board import Board
from model.cell.cell import Cell
from view.cell_view import CellView


class BoardView:
    board: Board
    cell_px: int

    def __init__(self, board: Board, cell_px: int =80, board_bg_color: Tuple[int, int, int] = Color):
        self.board = board
        self.cell_px = cell_px
        self.cell_view = CellView(cell_px)

    def draw_board(self, surface: pygame.Surface):
        surface.fill(Color(30, 30, 30))
        for row in self.board.cells:
            for current_cell in row:
                # IMPORTANT: Commented out the print statement to avoid performance issues and "infinite loop" perception.
                # print(f"Drawing cell ID: {current_cell.id} at coordinate: {current_cell.coordinate}")
                self.cell_view.draw_cell(cell=current_cell, surface=surface)
