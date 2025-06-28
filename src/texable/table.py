from typing import Optional, Any, Sequence, Union
import logging

from texable.column_alignments import ColumnAlignments
from texable.headers import Headers
from texable.line_borders import LineBorders
from texable.latex_builders import (
    make_caption,
    make_label,
    make_block,
    make_tabular_content,
    make_column_arg,
)
from texable.custom_types import Alignment

# Configure logging
logger = logging.getLogger(__name__)


class Table:
    """
    Represents a table for data manipulation and LaTeX generation.

    The `Table` class allows creating, modifying, and exporting tabular data
    with support for headers, column alignments, borders, captions, and labels.
    It can generate LaTeX code to include the table in LaTeX documents.

    Examples:
        Creating a table:

        >>> data = [
        ...     ["Name", "Age", "City"],
        ...     ["Alice", 30, "New York"],
        ...     ["Bob", 25, "Los Angeles"],
        ... ]
        >>> table = Table(data)

        Setting headers:

        >>> table.headers = ["Name", "Age", "City"]

        Setting column alignments:

        >>> from texable import Alignment
        >>> table.column_alignments = [Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT]

        Adding caption and label:

        >>> table.caption = "User Data"
        >>> table.label = "tab:user_data"

        Exporting LaTeX code:

        >>> latex_code = table.to_latex()
    """

    def __init__(self, data: Sequence[Sequence[Any]]) -> None:
        """
        Initialize a Table object.

        Args:
            data (Sequence[Sequence[Any]]): Data as a sequence of rows,
                each row a sequence of values.

        Raises:
            TypeError: If `data` is not a sequence of sequences.
            ValueError: If rows have inconsistent column counts.
        """
        if not isinstance(data, Sequence) or not all(
            isinstance(row, Sequence) for row in data
        ):
            raise TypeError("Data must be a sequence of sequences (rows).")

        self._data = data
        self._num_columns = len(data[0]) if data else 0
        self._num_rows = len(data)
        if not all(len(row) == self._num_columns for row in data):
            raise ValueError("All rows must have the same number of columns.")

        self._headers = Headers(self._num_columns)
        self._column_alignments = ColumnAlignments(self._num_columns)
        self._indent: str = "  "  # Default indentation for LaTeX blocks

        self._vertical_borders = LineBorders(self._num_columns + 1, is_horizontal=False)
        self._horizontal_borders = LineBorders(self._num_rows + 1, is_horizontal=True)

        self._table_alignment: Alignment = Alignment.CENTER
        self._caption: Optional[str] = None
        self._label: Optional[str] = None

    @property
    def headers(self) -> Headers:
        """
        Get or set the headers of the table.

        The headers must be a sequence of strings matching the number of columns.

        Returns:
            Headers: The table headers.

        Raises:
            TypeError: If assigned headers are not a sequence of strings.
            ValueError: If header count doesn't match number of columns.
        """
        return self._headers

    @headers.setter
    def headers(self, headers: Sequence[str]) -> None:
        if not isinstance(headers, Sequence):
            raise TypeError("Headers must be a sequence of strings.")
        if len(headers) != self._num_columns:
            raise ValueError(
                f"Number of headers ({len(headers)}) must match number of columns ({self._num_columns})."
            )

        self._headers[:] = headers

    @property
    def caption(self) -> Optional[str]:
        """
        Get or set the caption of the table.

        Overwriting an existing caption will log a warning.

        Returns:
            Optional[str]: Caption string or None if unset.
        """
        return self._caption

    @caption.setter
    def caption(self, caption: str) -> None:
        if self.caption is not None:
            logger.warning("Warning: Overwriting existing caption.")
        self._caption = str(caption)

    @property
    def label(self) -> Optional[str]:
        """
        Get or set the label of the table.

        Overwriting an existing label will log a warning.

        Returns:
            Optional[str]: Label string or None if unset.
        """
        return self._label

    @label.setter
    def label(self, label: str) -> None:
        if self.label is not None:
            logger.warning("Warning: Overwriting existing label.")
        self._label = str(label)

    @property
    def indent(self) -> str:
        """
        Get or set the indentation string used for LaTeX blocks.

        The default is two spaces.

        Returns:
            str: Indentation string.
        """
        return self._indent

    @indent.setter
    def indent(self, indent: str) -> None:
        self._indent = str(indent)

    @property
    def num_columns(self) -> int:
        """
        Get the number of columns in the table.

        Returns:
            int: Number of columns.
        """
        return self._num_columns

    @property
    def column_alignments(self) -> ColumnAlignments:
        """Get or set the alignments of the columns in the table.

        You can assign alignments using a single `Alignment` value or a sequence of `Alignment` values.
        - If a single `Alignment` is provided, it will be applied to all selected columns.
        - If a sequence is provided, it must match the number of columns being assigned.

        The default alignment for all columns is `Alignment.CENTER`.

        Returns:
            ColumnAlignments: Current column alignments.

        Raises:
            TypeError: If the input is not an `Alignment` or a sequence of `Alignment`.
            ValueError: If the number of alignments does not match the number of columns targeted.
            IndexError: If the specified index is out of range.

        Examples:
            Set all columns to left alignment:
            >>> table.column_alignments = Alignment.LEFT

            Set specific alignments for each column (assuming 3 columns):
            >>> table.column_alignments = [Alignment.LEFT, Alignment.CENTER, Alignment.RIGHT]

            Set individual columns:
            >>> table.column_alignments[0] = Alignment.LEFT

            Set a slice of columns:
            >>> table.column_alignments[1:3] = [Alignment.CENTER, Alignment.RIGHT]

            Set multiple columns using a tuple of indices:
            >>> table.column_alignments[0, 1] = Alignment.LEFT
        """
        return self._column_alignments

    @column_alignments.setter
    def column_alignments(
        self, alignments: Union[Alignment, Sequence[Alignment]]
    ) -> None:
        self._column_alignments[:] = alignments

    @property
    def vertical_borders(self) -> LineBorders:
        return self._vertical_borders

    @property
    def horizontal_borders(self) -> LineBorders:
        return self._horizontal_borders

    @property
    def table_alignment(self) -> Alignment:
        """Get or set the alignment of the table.

        The table alignment determines how the table is positioned within the LaTeX document.

        The default alignment is `Alignment.CENTER`.
        """
        return self._table_alignment

    @table_alignment.setter
    def table_alignment(self, alignment: Alignment) -> None:
        self._table_alignment = alignment

    def __str__(self) -> str:
        """
        Return the LaTeX string representation of the table.

        Returns:
            str: LaTeX code for the table.
        """
        tabular_alignment = self._table_alignment.table() + "\n"

        tabular_content = make_tabular_content(
            self._headers, self._data, self._horizontal_borders
        )
        tabular_block = make_block(
            name="tabular",
            content=tabular_content,
            indent=self._indent,
            required_arg=[
                make_column_arg(self._vertical_borders, self._column_alignments)
            ],
        )

        caption = make_caption(self._caption) if self._caption else ""
        label = make_label(self._label) if self._label else ""

        return make_block(
            name="table",
            content=f"{tabular_alignment}{tabular_block}{caption}{label}",
            indent=self._indent,
        )

    def to_latex(self) -> str:
        """
        Return the LaTeX string representation of the table.

        Returns:
            str: LaTeX code for the table.
        """
        return str(self)

    @classmethod
    def from_file(cls, file_path: str) -> "Table":
        """
        Create a Table object from a CSV or TSV file.

        Args:
            file_path (str): Path to a CSV (.csv) or TSV (.tsv) file.

        Returns:
            Table: A new Table instance with data loaded from the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file format is unsupported.
            ValueError: If rows have inconsistent column counts.
        """
        import os

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        match file_path:
            case file_path if file_path.endswith(".csv"):
                delimiter = ","
            case file_path if file_path.endswith(".tsv"):
                delimiter = "\t"
            case _:
                raise ValueError(
                    "Unsupported file format. Only .csv and .tsv files are supported."
                )

        # Read the file and create a Table instance
        with open(file_path, "r") as file:
            import csv

            reader = csv.reader(file, delimiter=delimiter)
            data = list(reader)

        return cls(data)

    def write_to_file(self, file_path: str) -> None:
        """
        Write the LaTeX representation of the table to a file.

        Args:
            file_path (str): Destination file path.
        """
        with open(file_path, "w") as file:
            file.write(str(self))

    def __repr__(self) -> str:
        """
        Return a string representation for debugging.

        Returns:
            str: A string representation of the Table object.
        """
        return f"Table(num_columns={self._num_columns}, num_rows={self._num_rows}, headers={self._headers})"
