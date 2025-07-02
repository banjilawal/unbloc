from dataclasses import dataclass, field
from typing import List, Optional

from exception.exception import InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from model.board.grid_coordinate import GridCoordinate
from model.occupant.crate import Crate
from common.dimension import Dimension
from model.occupant.escape_portal import EscapePortal
from model.occupant.boulder import Boulder
from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError
from src.model.cell.cell import Cell


@dataclass(frozen=True)
class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2

    id: int
    portal: EscapePortal

    crates: tuple[Crate, ...] = field(default_factory=tuple)
    boulders: tuple[Boulder, ...] = field(default_factory=tuple)
    cells: tuple[tuple[Cell, ...], ...] = field(init=False, repr=False)
    dimension: Dimension = field(default=Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

    def __post_init__(self):
        if self.id < GameDefault.MIN_ID:
            raise InvalidIdError("Board id below minimum value.")

        if self.dimension.height < self.MIN_ROW_COUNT:
            raise InvalidNumberOfRowsError()

        if self.dimension.length < self.MIN_COLUMN_COUNT:
            raise InvalidNumberOfColumnsError

        # Create the grid of cells
        rows = tuple(
            tuple(
                Cell(id=self.dimension.height * self.dimension.length + column + 1,
                     coordinate=GridCoordinate(row=self.dimension.height, column=self.dimension.length))
                for column in range(self.dimension.length)
            )
        )
        object.__setattr__(self, 'cells', rows)
        # rows = []
        # for row in range(self.row_count):
        #     current_row = []
        #     for column in range(self.column_count):
        #         cell_id = row * self.column_count + column + 1
        #         cell = Cell(id=cell_id, coordinate=GridCoordinate(row=row, column=column))
        #         current_row.append(cell)
        #     rows.append(tuple(current_row))
        # object.__setattr__(self, 'cells', tuple(rows))

    @@property
    def row_count(self) -> int:
        return self.dimension.height

    @@property
    def column_count(self) -> int:
        return self.dimension.length


    def print(self):
        """Print the board with cell IDs"""
        for row in self.cells:
            # Top border of the row
            print("".join("+---" for _ in row) + "+")
            # Cell IDs in the row, centered in each cell
            print("".join(f"|{cell.id:^3}" for cell in row) + "|")
        # Bottom border of the final row
        print("".join("+---" for _ in self.cells[0]) + "+")