from typing import Sequence, overload
from texable.cell import Cell


class Row(Sequence[Cell]):
    """
    Represents a row in a table.
    """

    def __init__(self, cells: Sequence[Cell]) -> None:
        """
        Initializes a Row with the given cells.

        Args:
            cells (Sequence[Cell]): A sequence of Cell objects representing the row.
        """
        self._cells = cells

    def add_formatters(self, *formatters) -> None:
        """
        Adds formatters to all cells in the row.

        Args:
            *formatters: Formatters to apply to each cell in the row.
        """
        for cell in self._cells:
            cell.add_formatters(*formatters)

    @overload
    def __getitem__(self, index: int) -> Cell: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[Cell]: ...

    def __getitem__(self, index):
        """
        Gets the cell at the specified index or slice.

        Args:
            index (int or slice): The index or slice of the cell(s) to retrieve.

        Returns:
            Cell or Sequence[Cell]: The cell at the specified index or a sequence of cells for a slice.
        """
        return self._cells[index]

    def __len__(self) -> int:
        """
        Returns the number of cells in the row.

        Returns:
            int: The number of cells in the row.
        """
        return len(self._cells)

    def __iter__(self):
        """
        Returns an iterator over the cells in the row.

        Returns:
            Iterator[Cell]: An iterator over the cells in the row.
        """
        return iter(self._cells)

    def __str__(self) -> str:
        """
        Returns a string representation of the row.

        Returns:
            str: A string representation of the row.
        """
        return " | ".join(str(cell) for cell in self._cells)

    def __repr__(self) -> str:
        """
        Returns a string representation of the row.

        Returns:
            str: A string representation of the row.
        """
        return f"Row({self._cells})"

    def to_latex(self) -> str:
        """
        Converts the row to a LaTeX formatted string.

        Returns:
            str: A LaTeX formatted string representing the row.
        """
        return " & ".join(cell.to_latex() for cell in self._cells) + r" \\" + "\n"
