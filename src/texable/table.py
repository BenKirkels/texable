from typing import Optional, Any, Sequence, Union
import logging

from texable.alignments import Alignments
from texable.headers import Headers
from texable.vertical_borders import VerticalBorders
from texable.latex_builders import (
    make_caption,
    make_label,
    make_block,
    make_tabular_content,
)
import texable.custom_types as types

# Configure logging
logger = logging.getLogger(__name__)


class Table:
    def __init__(self, data: Sequence[Sequence[Any]]) -> None:
        """Initialize a Table object."""

        if not isinstance(data, Sequence) or not all(
            isinstance(row, Sequence) for row in data
        ):
            raise TypeError("Data must be a sequence of sequences (rows).")

        self._num_columns = len(data[0]) if data else 0
        assert all(
            len(row) == self._num_columns for row in data
        ), "All rows must have the same number of columns."

        self._num_rows = len(data)

        self._data = data

        self._headers = Headers(self._num_columns)
        self._alignments = Alignments(self._num_columns)
        self._indent: str = "  "  # Default indentation for LaTeX blocks

        self._vertical_borders = VerticalBorders(self._num_columns)

        self._table_alignment: types.alignment = "center"

        self._caption: Optional[str] = None
        self._label: Optional[str] = None

    @property
    def headers(self) -> Headers:
        return self._headers

    @headers.setter
    def headers(self, headers: Sequence[str]) -> None:
        self._headers[:] = headers

    @property
    def caption(self) -> Optional[str]:
        return self._caption

    @caption.setter
    def caption(self, caption: str) -> None:
        if self.caption is not None:
            logger.warning("Warning: Overwriting existing caption.")
        self._caption = str(caption)

    @property
    def label(self) -> Optional[str]:
        return self._label

    @label.setter
    def label(self, label: str) -> None:
        if self.label is not None:
            logger.warning("Warning: Overwriting existing label.")
        self._label = str(label)

    @property
    def indent(self) -> str:
        return self._indent

    @indent.setter
    def indent(self, indent: str) -> None:
        self._indent = str(indent)

    @property
    def num_columns(self) -> int:
        return self._num_columns

    @property
    def alignments(self) -> Alignments:
        return self._alignments

    @alignments.setter
    def alignments(self, alignments: Union[str, Sequence[str]]) -> None:
        self._alignments[:] = alignments

    @property
    def vertical_borders(self) -> VerticalBorders:
        return self._vertical_borders

    def set_table_alignment(self, alignment: types.alignment) -> None:
        """Set the alignment of the entire table."""
        if alignment not in {"center", "left", "right"}:
            raise ValueError("Alignment must be 'center', 'left', or 'right'.")
        self._table_alignment = alignment

    def __str__(self) -> str:
        alignment_map = {
            "center": "\\centering\n",
            "left": "\\raggedright\n",
            "right": "\\raggedleft\n",
        }
        tabular_alignment = alignment_map.get(self._table_alignment, "")

        tabular_content = make_tabular_content(self._headers, self._data)
        tabular_block = make_block(
            name="tabular",
            content=tabular_content,
            indent=self._indent,
            required_arg=[self._column_arg()],
        )

        caption = make_caption(self._caption) if self._caption else ""
        label = make_label(self._label) if self._label else ""

        return make_block(
            name="table",
            content=f"{tabular_alignment}{tabular_block}{caption}{label}",
            indent=self._indent,
        )

    def write_to_file(self, file_path: str) -> None:
        with open(file_path, "w") as file:
            file.write(str(self))

    def __repr__(self) -> str:
        return f"Table(header={self._headers}, rows={self._data})"

    def _column_arg(self) -> str:
        """Generate the column argument for the tabular environment."""
        result = ""
        for i in range(self._num_columns):
            result += self._vertical_borders[i]
            result += self._alignments[i]
        result += self._vertical_borders[self._num_columns]
        return result
