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
