from typing import Union, Sequence


class ColumnAlignments:
    def __init__(self, num_columns: int) -> None:
        if not isinstance(num_columns, int) or num_columns <= 0:
            raise ValueError("Number of columns must be a positive integer.")

        self._alignments: list[str] = [
            "c"
        ] * num_columns  # Default to center alignment for all columns

    @property
    def alignments(self) -> list[str]:
        """Get the list of alignments."""
        return self._alignments.copy()

    def __setitem__(
        self, index: Union[int, slice, tuple], value: Union[str, Sequence[str]]
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
        VALID_ALIGNMENTS = {"l", "c", "r"}

        def validate_alignment(val: str) -> None:
            if val not in VALID_ALIGNMENTS:
                raise ValueError("Alignment must be one of 'l', 'c', or 'r'.")

        if isinstance(index, int):
            if not isinstance(value, str):
                raise TypeError("Alignment must be a string.")
            if index < 0 or index >= len(self._alignments):
                raise IndexError("Index out of range.")
            validate_alignment(value)
            self._alignments[index] = value

        elif isinstance(index, (slice, tuple)):
            if isinstance(index, tuple):
                indexes = list(index)
                if any(not isinstance(i, int) for i in indexes):
                    raise TypeError("All indices must be integers.")

            elif isinstance(index, slice):
                indexes = list(range(*index.indices(len(self._alignments))))

            if isinstance(value, str):
                value = [value] * len(indexes)

            if isinstance(value, Sequence):
                if len(value) != len(indexes):
                    raise ValueError(
                        "Number of alignments must match the number of indices."
                    )
                for i, val in zip(indexes, value):
                    if not isinstance(val, str):
                        raise TypeError("Each alignment must be a string.")
                    validate_alignment(val)
                    self._alignments[i] = val
            else:
                raise TypeError("Value must be a string or a sequence of strings.")

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
        return "".join(self._alignments)
