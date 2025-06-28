from typing import Callable


class Cell[T]:
    """
    Represents a cell in a table with its content and formatting options.
    """

    def __init__(self, content: T) -> None:
        """
        Initializes a Cell with the given content.

        Args:
            content (T): The content of the cell, which can be of any type.
        """
        self._content = content
        self._formatters: list[Callable[[str], str]] = []

    @property
    def content(self) -> T:
        """
        Returns the content of the cell.

        Returns:
            T: The content of the cell.
        """
        return self._content

    @content.setter
    def content(self, value: T) -> None:
        """
        Sets the content of the cell.

        Args:
            value (T): The new content for the cell.
        """

        self._content = value

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
        return str(self._content)

    def __repr__(self) -> str:
        """
        Returns a string representation of the cell's content.

        Returns:
            str: A string representation of the cell.
        """
        return f"Cell({self._content})"

    def to_latex(self) -> str:
        """
        Converts the cell's content to a LaTeX string, applying any formatters.
        Returns:
            str: The LaTeX representation of the cell's content.
        """
        content_str = str(self._content)
        for formatter in self._formatters:
            content_str = formatter(content_str)
        return content_str
