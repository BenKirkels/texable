from typing import Sequence

from texable.cell import Cell
from texable.row import Row


class Grid[T]:
    """
    A class to represent a grid of cells.
    """

    def __init__(self, data: Sequence[Sequence[T]]) -> None:
        """
        Initializes the Grid with the provided data.

        Args:
            data (Sequence[Sequence[T]]): A 2D sequence representing the grid data.
        """
        self._num_rows = len(data)
        self._num_cols = len(data[0])
        if any(len(row) != self._num_cols for row in data):
            raise ValueError("All rows must have the same number of columns.")

        self._grid = [Row([Cell(value) for value in row]) for row in data]

    @property
    def rows(self) -> list[Row]:
        """
        Returns the rows of the grid.
        Returns:
            Sequence[Row]: A sequence of Row objects representing the grid rows.
        """
        return self._grid

    def __getitem__(self, index: int) -> Row:
        """
        Gets the row at the specified index.

        Args:
            index (int): The index of the row to retrieve.

        Returns:
            List[Cell[T]]: The row at the specified index.
        """
        return self._grid[index]

    @property
    def num_rows(self) -> int:
        """
        Returns the number of rows in the grid.

        Returns:
            int: The number of rows.
        """
        return self._num_rows

    @property
    def num_cols(self) -> int:
        """
        Returns the number of columns in the grid.

        Returns:
            int: The number of columns.
        """
        return self._num_cols

    def __str__(self) -> str:
        columns = [[] for _ in range(self.num_cols)]
        for row in self._grid:
            for i, cell in enumerate(row):
                columns[i].append(str(cell))
        col_widths = [max(len(cell) for cell in col) for col in columns]

        def format_row(row):
            return " | ".join(
                f"{str(cell):<{col_widths[i]}}" for i, cell in enumerate(row)
            )

        result = ""
        for row in self._grid:
            result += format_row(row) + "\n"

        return result.strip()

    def __repr__(self) -> str:
        """
        Returns a string representation of the grid.

        Returns:
            str: A string representation of the grid.
        """
        return "\n".join([" | ".join(repr(cell) for cell in row) for row in self._grid])

    def __iter__(self):
        """
        Returns an iterator over the rows of the grid.

        Returns:
            Iterator[List[Cell[T]]]: An iterator over the rows.
        """
        return iter(self._grid)


if __name__ == "__main__":
    # Example usage
    grid_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    grid = Grid(grid_data)
    print(grid)
    print()
    print(grid[1])
    print()
    print(grid[1][0])
