from typing import Callable, Optional, Sequence
from texable.cell import Cell


class Row(list[Cell]):
    """
    Represents a row in a table.
    """

    def __init__(self, cells: Sequence[Cell]) -> None:
        """
        Initializes a Row with the given cells.

        Args:
            cells (Sequence[Cell]): A sequence of Cell objects representing the row.
        """
        super().__init__(cells)

    def add_formatters(
        self,
        *formatters: Callable[[str], str],
        selector: Optional[Callable[[Cell], bool]] = None,
    ) -> None:
        """
        Adds formatters to all cells in the row.

        Args:
            *formatters: Formatters to apply to each cell in the row.
        """
        for cell in self:
            if selector is None or selector(cell):
                cell.add_formatters(*formatters)

    def __str__(self) -> str:
        """
        Returns a string representation of the row.

        Returns:
            str: A string representation of the row.
        """
        return " | ".join(str(cell) for cell in self)

    def __repr__(self) -> str:
        """
        Returns a string representation of the row.

        Returns:
            str: A string representation of the row.
        """
        return f"Row({self})"

    def to_latex(self) -> str:
        """
        Converts the row to a LaTeX formatted string.

        Returns:
            str: A LaTeX formatted string representing the row.
        """
        return " & ".join(cell.to_latex() for cell in self) + r" \\" + "\n"
