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

# Configure logging
logger = logging.getLogger(__name__)


class Table:
    def __init__(self, num_columns: int):
        self._num_columns = num_columns
        self._rows: list[list[Any]] = []

        self._headers = Headers(num_columns)
        self._alignments = Alignments(num_columns)
        self._indent: str = "  "  # Default indentation for LaTeX blocks

        self._vertical_borders = VerticalBorders(num_columns)

        self._caption: Optional[str] = None
        self._label: Optional[str] = None

    def add_rows(self, rows: Sequence[Sequence[Any]]) -> None:
        for row in rows:
            row = list(row)

            if len(row) != self.num_columns:
                raise ValueError(
                    f"Row length must match the number of columns ({self.num_columns})."
                )

            self._rows.append(row)

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

    def __str__(self) -> str:
        tabular_content = make_tabular_content(self._headers, self._rows)
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
            content=tabular_block + caption + label,
            indent=self._indent,
        )

    def write_to_file(self, file_path: str) -> None:
        with open(file_path, "w") as file:
            file.write(str(self))

    def __repr__(self) -> str:
        return f"Table(header={self._headers}, rows={self._rows})"

    def _column_arg(self) -> str:
        """Generate the column argument for the tabular environment."""
        result = ""
        for i in range(self._num_columns):
            result += self._vertical_borders[i]
            result += self._alignments[i]
        result += self._vertical_borders[self._num_columns]
        return result
