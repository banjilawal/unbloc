from typing import List

from common.id_generator import IdGenerator
from model.board.grid_coordinate import GridCoordinate
from model.occupant.escape_portal import EscapePortal
from model.occupant.boulder import Boulder
from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError, InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from src.model.cell.cell import Cell


@dataclass(frozen=True)
class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2

    id: int
    portal: EscapePortal

    # Unified occupant storage
    occupants: List[Occupant] = field(default_factory=list)

    # 2D list of immutable cells that is filled after Board initialization
    cells: tuple[tuple[Cell, ...], ...] = field(init=False, repr=False)

    row_count: int = field(default=GameDefault.ROW_COUNT)
    column_count: int = field(default=GameDefault.COLUMN_COUNT)

    def __post_init__(self):
        if self.id < GameDefault.MIN_ID:
            raise InvalidIdError("Board id below minimum value.")
        if self.row_count < Board.MIN_ROW_COUNT:
            raise InvalidNumberOfRowsError("Board num_rows below minimum value.")
        if self.column_count < Board.MIN_COLUMN_COUNT:
            raise InvalidNumberOfColumnsError("Board num_columns below minimum value.")

        # Create the grid of cells
        rows = []
        for row in range(self.row_count):
            current_row = []
            for column in range(self.column_count):
                cell_id = row * self.column_count + column + 1
                cell = Cell(id=cell_id, coordinate=GridCoordinate(row=row, column=column))
                current_row.append(cell)
            rows.append(tuple(current_row))
        object.__setattr__(self, 'cells', tuple(rows))

        # Assign portal and occupants to this board (set their colors)
        self._assign_occupants_to_board()

    def _assign_occupants_to_board(self):
        """Assign all occupants to this board by setting their colors"""
        # Portal gets portal color
        if self.portal.color is None:
            object.__setattr__(self.portal, 'color', GameDefault.PORTAL_COLOR)

        # Other occupants get their default colors
        for occupant in self.occupants:
            if occupant.color is None:
                if isinstance(occupant, Boulder):
                    object.__setattr__(occupant, 'color', GameDefault.OBSTACLE_COLOR)
                elif isinstance(occupant, Crate):
                    object.__setattr__(occupant, 'color', GameDefault.OBSTACLE_COLOR)

    def area(self):
        return self.row_count * self.column_count

    def get_all_occupants(self) -> List[Occupant]:
        """Get all occupants on this board including the portal"""
        return [self.portal] + self.occupants

    def get_boulders(self) -> List[Boulder]:
        """Get all boulders on this board"""
        return [occ for occ in self.occupants if isinstance(occ, Boulder)]

    def get_crates(self) -> List[Crate]:
        """Get all crates on this board"""
        return [occ for occ in self.occupants if isinstance(occ, Crate)]

    def place_occupant(self, occupant: Occupant, coordinate: GridCoordinate):
        """Place an occupant on the board at the given coordinate"""
        if not self._is_valid_coordinate(coordinate):
            raise InvalidCoordinateError(f"Coordinate {coordinate} is outside board bounds")

        if self.is_coordinate_occupied(coordinate):
            raise OccupiedSquareEntryError(f"Coordinate {coordinate} is already occupied")

        # Check if occupant fits within board bounds
        if not self._occupant_fits_at_coordinate(occupant, coordinate):
            raise InvalidPlacementError(f"Occupant doesn't fit at coordinate {coordinate}")

        # Place the occupant
        object.__setattr__(occupant, 'coordinate', coordinate)

    def is_coordinate_occupied(self, coordinate: GridCoordinate) -> bool:
        """Check if a coordinate is occupied by any occupant"""
        for occupant in self.get_all_occupants():
            if occupant.is_placed() and coordinate in occupant.get_occupied_coordinates():
                return True
        return False

    def get_occupant_at_coordinate(self, coordinate: GridCoordinate) -> Optional[Occupant]:
        """Get the occupant at the given coordinate, if any"""
        for occupant in self.get_all_occupants():
            if occupant.is_placed() and coordinate in occupant.get_occupied_coordinates():
                return occupant
        return None

    def _is_valid_coordinate(self, coordinate: GridCoordinate) -> bool:
        """Check if coordinate is within board bounds"""
        return (0 <= coordinate.row < self.row_count and
                0 <= coordinate.col < self.column_count)

    def _occupant_fits_at_coordinate(self, occupant: Occupant, coordinate: GridCoordinate) -> bool:
        """Check if occupant fits on board when placed at coordinate"""
        end_row = coordinate.row + occupant.dimension.height - 1
        end_col = coordinate.col + occupant.dimension.length - 1

        return (end_row < self.row_count and end_col < self.column_count)

    def print(self):
        """Print the board with cell IDs"""
        for row in self.cells:
            # Top border of the row
            print("".join("+---" for _ in row) + "+")
            # Cell IDs in the row, centered in each cell
            print("".join(f"|{cell.id:^3}" for cell in row) + "|")
        # Bottom border of the final row
        print("".join("+---" for _ in self.cells[0]) + "+")