from typing import Any, Callable, Generic, TypeVar
from functools import total_ordering

T = TypeVar("T")


@total_ordering
class Cell(Generic[T]):
    """
    Represents a cell in a table with its content and formatting options.
    """

    def __init__(self, value: T) -> None:
        """
        Initializes a Cell with the given content.

        Args:
            content (T): The content of the cell, which can be of any type.
        """
        self._value = value
        self._formatters: list[Callable[[str], str]] = []

    @property
    def value(self) -> T:
        """
        Returns the content of the cell.

        Returns:
            T: The content of the cell.
        """
        return self._value

    @value.setter
    def value(self, value: T) -> None:
        """
        Sets the content of the cell.

        Args:
            value (T): The new content for the cell.
        """

        self._value = value

    def add_formatters(self, *formatters: Callable[[str], str]) -> None:
        """
        Adds formatters to the cell's content.

        Args:
            *formatters (Callable[[str], str]): Formatters to apply to the cell's content.
        """
        self._formatters.extend(formatters)

    def __str__(self) -> str:
        """
        Returns a string representation of the cell's content.

        Returns:
            str: The string representation of the cell's content.
        """
        return str(self._value)

    def __repr__(self) -> str:
        """
        Returns a string representation of the cell's content.

        Returns:
            str: A string representation of the cell.
        """
        return f"Cell({self._value})"

    def to_latex(self) -> str:
        """
        Converts the cell's content to a LaTeX string, applying any formatters.
        Returns:
            str: The LaTeX representation of the cell's content.
        """
        content_str = str(self._value)
        for formatter in self._formatters:
            content_str = formatter(content_str)
        return content_str

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Cell):
            return self._value == other._value
        try:
            return self._value == other
        except Exception:
            return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Cell):
            return self._value < other._value
        try:
            return self._value < other
        except Exception:
            return NotImplemented
