from typing import Sequence, Union


class Headers:
    def __init__(self, num_headers: int) -> None:
        self._headers: list[str] = [""] * num_headers  # Initialize with empty strings

    @property
    def headers(self) -> list[str]:
        """Get the list of headers."""
        return self._headers

    def __getitem__(self, index: int) -> str:
        return self._headers[index]

    def __setitem__(
        self, index: Union[int, slice, tuple], value: Union[str, Sequence[str]]
    ) -> None:
        if isinstance(index, int):
            if not isinstance(value, str):
                raise TypeError(f"Header must be a string, got {type(value).__name__}.")
            if index < 0 or index >= len(self._headers):
                raise IndexError("Index out of range")
            self._headers[index] = str(value)

        elif isinstance(index, (slice, tuple)):
            if isinstance(index, tuple):
                indexes = list(index)
            elif isinstance(index, slice):
                indexes = list(range(*index.indices(len(self._headers))))

            if isinstance(value, str):
                value = [value] * len(indexes)

            if isinstance(value, Sequence):
                if len(value) != len(indexes):
                    raise ValueError(
                        f"Length of value list must match the number of indices."
                    )
                for i, val in zip(indexes, value):
                    if not isinstance(val, str):
                        raise TypeError(
                            f"Header must be a string, got {type(val).__name__}."
                        )
                    self._headers[i] = str(val)
            else:
                raise TypeError(
                    f"Value must be a string or a sequence of strings, got {type(value).__name__}."
                )

        else:
            raise TypeError(
                f"Index must be an integer or a slice, got {type(index).__name__}."
            )

    def __len__(self) -> int:
        return len(self._headers)

    def __iter__(self):
        return iter(self._headers)

    def __repr__(self):
        return repr(self._headers)
