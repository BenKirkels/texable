from typing import Union


class Alignments:
    def __init__(self, num_columns: int) -> None:
        if not isinstance(num_columns, int) or num_columns <= 0:
            raise ValueError("Number of columns must be a positive integer.")

        self._alignments: list[str] = [
            "c"
        ] * num_columns  # Default to center alignment for all columns

    def __setitem__(
        self, index: Union[int, slice], value: Union[str, list[str]]
    ) -> None:
        """Set the alignment for one or more columns.

        Args:
            index (Union[int, slice]): The index or slice of columns to set.
            value (Union[str, list[str]]): The alignment value(s) to set.
            Must be one of 'l', 'c', or 'r' for left, center, or right alignment.
        Raises:
            TypeError: If the index is not an integer or slice, or if the value is not a string or list of strings.
            ValueError: If the alignment value is not one of 'l', 'c', or 'r', or if the length of the value list does not match the number of indices.
            IndexError: If the index is out of range.
        """
        if isinstance(index, slice):
            indexes = range(
                index.start or 0, index.stop or len(self._alignments), index.step or 1
            )

            if isinstance(value, list):
                if len(value) != len(indexes):
                    raise ValueError(
                        "Length of value list must match the number of indices."
                    )
                for i, val in zip(indexes, value):
                    self.__setitem__(i, val)
            elif isinstance(value, str):
                for i in indexes:
                    self.__setitem__(i, value)
        elif isinstance(index, int):
            if not isinstance(value, str):
                raise TypeError("Alignment must be a string.")
            if value not in ("l", "c", "r"):
                raise ValueError("Alignment must be one of 'l', 'c', or 'r'.")
            if index < 0 or index >= len(self._alignments):
                raise IndexError("Index out of range")
            self._alignments[index] = value
        else:
            raise TypeError("Index must be an integer or a slice.")

    def __getitem__(self, index: int) -> str:
        if index < 0 or index >= len(self._alignments):
            raise IndexError("Index out of range")
        return self._alignments[index]

    def __len__(self) -> int:
        return len(self._alignments)

    def __iter__(self):
        return iter(self._alignments)

    def __str__(self) -> str:
        return " ".join(self._alignments)
