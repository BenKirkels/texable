from typing import Union


class VerticalBorders:
    def __init__(self, num_columns: int) -> None:
        self._num_columns = num_columns
        self._edges = [False] * (num_columns + 1)

    @property
    def edges(self) -> list[bool]:
        """Get the list of vertical edges."""
        return self._edges.copy()

    def enable_all(self) -> None:
        """Enable all vertical edges."""
        for i in range(len(self._edges)):
            self._edges[i] = True

    def enable_outer(self) -> None:
        """Enable only the outer vertical edges (first and last)."""
        self._edges[0] = True
        self._edges[-1] = True

    def enable(self, *indexes: int) -> None:
        """Enable a specific vertical edge or edges."""
        for index in indexes:
            if not isinstance(index, int):
                raise TypeError("Index must be an integer.")
            if index < 0 or index >= self._num_columns + 1:
                raise IndexError("Index out of range.")
            self._edges[index] = True

    def __getitem__(self, index: int) -> str:
        """Get the status of a specific vertical edge."""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._num_columns + 1:
            raise IndexError("Index out of range.")

        return "|" if self._edges[index] else ""
