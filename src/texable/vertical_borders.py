class VerticalBorders:
    def __init__(self, num_columns: int) -> None:
        self._num_columns = num_columns
        self._borders = [False] * (num_columns + 1)

    @property
    def borders(self) -> list[bool]:
        """Get the list of vertical borders."""
        return self._borders.copy()

    def all(self) -> None:
        """Enable all vertical borders."""
        for i in range(len(self._borders)):
            self._borders[i] = True

    def outer(self) -> None:
        """Enable only the outer vertical borders (first and last)."""
        self._borders[0] = True
        self._borders[-1] = True

    def inner(self) -> None:
        """Enable only the inner vertical borders (excluding the first and last)."""
        for i in range(1, len(self._borders) - 1):
            self._borders[i] = True

    def at(self, *indexes: int) -> None:
        """Enable a specific vertical edge or borders."""
        for index in indexes:
            if not isinstance(index, int):
                raise TypeError("Index must be an integer.")
            if index < 0 or index >= self._num_columns + 1:
                raise IndexError("Index out of range.")
            self._borders[index] = True

    def __getitem__(self, index: int) -> str:
        """Get the status of a specific vertical edge."""
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._num_columns + 1:
            raise IndexError("Index out of range.")

        return "|" if self._borders[index] else ""
