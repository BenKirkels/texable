from typing import Optional, Any, Sequence, Union
import logging

from texable.alignments import Alignments
from texable.headers import Headers

# Configure logging
logger = logging.getLogger(__name__)


class Table:
    def __init__(self, num_columns: int):
        self._num_columns = num_columns
        self._rows: list[list[Any]] = []

        self._headers = Headers(num_columns)
        self._alignments = Alignments(num_columns)
        self._indent: str = "  "  # Default indentation for LaTeX blocks

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

    def __str__(self) -> str:
        tabular_content = self._build_tabular_content()
        tabular_block = self._latex_block(
            "tabular",
            tabular_content,
            required_arg=[self._column_format()],
        )
        return self._latex_block(
            "table",
            tabular_block + self._make_caption() + self._make_label(),
        )

    def write_to_file(self, file_path: str) -> None:
        with open(file_path, "w") as file:
            file.write(str(self))

    def __repr__(self) -> str:
        return f"Table(header={self._headers}, rows={self._rows})"

    # ========== Internal Utilities ==========
    def _format_row(self, row: Sequence[Any]) -> str:
        return " & ".join(str(cell) for cell in row) + r" \\" + "\n"

    def _column_format(self) -> str:
        return str(self.alignments)

    def _make_caption(self) -> str:
        return f"\\caption{{{self.caption}}}\n" if self.caption else ""

    def _make_label(self) -> str:
        return f"\\label{{{self.label}}}\n" if self.label else ""

    def _build_tabular_content(self) -> str:
        all_rows = (
            [self.headers.headers] + self._rows if self.headers.are_set else self._rows
        )
        return "".join(self._format_row(row) for row in all_rows)

    def _latex_block(
        self,
        name: str,
        content: str,
        required_arg: Optional[list[str]] = None,
        optional_arg: Optional[list[str]] = None,
    ) -> str:
        required = f"{{{', '.join(required_arg)}}}" if required_arg else ""
        optional = f"[{', '.join(optional_arg)}]" if optional_arg else ""
        indented = "\n".join(
            self.indent + line if line.strip() else "" for line in content.splitlines()
        )
        return f"\\begin{{{name}}}{required}{optional}\n{indented}\n\\end{{{name}}}\n"
