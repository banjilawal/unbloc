from dataclasses import dataclass
from typing import Optional

@dataclass
class GameCoordinate:
    id: int
    row: int
    colum: int

    @property
    def id(self) -> int:
        return self.id

    @property
    def row(self) -> int:
        return self.row

    @property
    def column(self) -> int:
        return self.column