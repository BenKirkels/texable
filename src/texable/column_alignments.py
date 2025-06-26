from typing import Union, Sequence

from texable.custom_types import Alignment


class ColumnAlignments:
    def __init__(self, num_columns: int) -> None:
        if not isinstance(num_columns, int) or num_columns <= 0:
            raise ValueError("Number of columns must be a positive integer.")

        self._alignments: list[Alignment] = [
            Alignment.CENTER  # Default alignment is center
        ] * num_columns  # Default to center alignment for all columns

    @property
    def alignments(self) -> list[str]:
        """Get the list of alignments."""
        return [a.column() for a in self._alignments]

    def __setitem__(
        self,
        index: Union[int, slice, tuple],
        value: Union[Alignment, Sequence[Alignment]],
    ) -> None:
        """Set the alignment for one or more columns.

        Args:
            index : The index or slice of columns to set.
            value : The alignment value(s) to set.
                Must be one of 'l', 'c', or 'r' for left, center, or right alignment.
        Raises:
            TypeError: If the index is not an integer or slice, or if the value is not a string or list of strings.
            ValueError: If the alignment value is not one of 'l', 'c', or 'r', or if the length of the value list does not match the number of indices.
            IndexError: If the index is out of range.
        """

        if isinstance(index, int):
            if not isinstance(value, Alignment):
                raise TypeError("Alignment must be an Alignment.")
            if index < 0 or index >= len(self._alignments):
                raise IndexError("Index out of range.")
            self._alignments[index] = value

        elif isinstance(index, (slice, tuple)):
            if isinstance(index, tuple):
                indexes = list(index)
                if any(not isinstance(i, int) for i in indexes):
                    raise TypeError("All indices must be integers.")

            elif isinstance(index, slice):
                indexes = list(range(*index.indices(len(self._alignments))))

            if isinstance(value, Alignment):
                value = [value] * len(indexes)

            if isinstance(value, Sequence):
                if len(value) != len(indexes):
                    raise ValueError(
                        "Number of alignments must match the number of indices."
                    )
                for i, val in zip(indexes, value):
                    if not isinstance(val, Alignment):
                        raise TypeError("Each alignment must be an Alignment.")
                    self._alignments[i] = val
            else:
                raise TypeError(
                    "Value must be an Alignment or a sequence of Alignments."
                )

        else:
            raise TypeError("Index must be an integer or a slice.")

    def __getitem__(self, index: int) -> str:
        if index >= len(self._alignments):
            raise IndexError("Index out of range")
        return self._alignments[index].column()

    def __len__(self) -> int:
        return len(self._alignments)

    def __iter__(self):
        return iter(self._alignments)

    def __str__(self) -> str:
        return "".join([a.column() for a in self._alignments])
