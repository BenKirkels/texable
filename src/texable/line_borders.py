from typing import Literal
from abc import ABC, abstractmethod


class LineBorders(ABC):
    """
    Represents borders between adjacent cells along one axis (horizontal or vertical).
    This class does not represent all borders of a grid, only those between elements
    along one direction.

    For example, in a grid with 4 columns, Vertical LineBorders would track the 5 vertical
    borders (between and around the columns).
    """

    def __init__(self, num_borders: int) -> None:
        self._num_borders = num_borders
        self._borders = [""] * num_borders

    @property
    def borders(self) -> list[str]:
        """Get the list of borders."""
        return self._borders.copy()

    def all(self, type: Literal["single", "double"] = "single") -> None:
        """Enable all borders."""
        for i in range(len(self._borders)):
            self.at(i, type)

    def outer(self, type: Literal["single", "double"] = "single") -> None:
        """Enable only the outer borders (first and last)."""
        self.at(0, type)
        self.at(-1, type)

    def inner(self, type: Literal["single", "double"] = "single") -> None:
        """Enable only the inner borders (excluding the first and last)."""
        for i in range(1, len(self._borders) - 1):
            self.at(i, type)

    def at(self, index: int, type: Literal["single", "double"] = "single") -> None:
        """Enable a specific border."""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index >= self._num_borders:
            raise IndexError("Index out of range.")

        self._borders[index] = self._make_border(type)

    @abstractmethod
    def _make_border(self, type: Literal["single", "double"]) -> str:
        """Abstract method to define how to create a border."""
        pass

    def __getitem__(self, index: int) -> str:
        """Get the status of a specific border."""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index >= self._num_borders:
            raise IndexError("Index out of range.")

        return self._borders[index]

    def __len__(self) -> int:
        """Get the number of borders."""
        return self._num_borders


class HorizontalBorders(LineBorders):
    """
    Represents horizontal borders between rows in a table.
    This class is a specialized version of `LineBorders` for horizontal borders.
    """

    def _make_border(self, type: Literal["single", "double"]) -> str:
        """Define how to create a horizontal border."""
        return "\\hline" if type == "single" else "\\hline\\hline"


class VerticalBorders(LineBorders):
    """
    Represents vertical borders between columns in a table.
    This class is a specialized version of `LineBorders` for vertical borders.
    """

    def _make_border(self, type: Literal["single", "double"]) -> str:
        """Define how to create a vertical border."""
        return "|" if type == "single" else "||"
