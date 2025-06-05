from typing import Optional, Self, Iterable, Any
import logging

# Configure logging
logger = logging.getLogger(__name__)


class Table:
    def __init__(self):
        self.header: list[Any] = []
        self.rows: list[list[Any]] = []
        self.caption: Optional[str] = None
        self.label: Optional[str] = None
        self.indent: str = "  "  # Default indentation for LaTeX blocks

    def set_header(self, header: Iterable[Any]) -> Self:
        self._validate_iterable(header, "header")
        header = list(header)

        if self.rows and len(header) != len(self.rows[0]):
            raise ValueError("Header length must match number of columns in rows")

        if self.header:
            logger.warning("Overwriting existing header.")

        self.header = header
        return self

    def add_rows(self, rows: Iterable[Iterable[Any]]) -> Self:
        for row in rows:
            self._validate_iterable(row, "row")
            row = list(row)

            if self.header and len(row) != len(self.header):
                raise ValueError("Row length must match the header length.")
            if not self.header and len(row) != len(self.rows[0]) if self.rows else 0:
                raise ValueError("Row length must match the number of columns.")

            self.rows.append(row)

        return self

    def set_caption(self, caption: str) -> Self:
        self._validate_string(caption, "caption")

        if self.caption is not None:
            print("Warning: Overwriting existing caption.")

        self.caption = caption
        return self

    def set_label(self, label: str) -> Self:
        self._validate_string(label, "label")

        if self.label is not None:
            print("Warning: Overwriting existing label.")

        self.label = label
        return self

    def set_indent(self, indent: str) -> Self:
        self._validate_string(indent, "indent")
        self.indent = indent
        return self

    def __str__(self) -> str:
        tabular_content = self._build_tabular_content()
        tabular_block = self._latex_block(
            "tabular",
            tabular_content,
            required_arg=[self._column_format()],
        )
        return "\n" + self._latex_block(
            "table",
            tabular_block + self._caption() + self._label(),
        )

    def write_to_file(self, file_path: str) -> None:
        with open(file_path, "w") as file:
            file.write(str(self))

    def __repr__(self) -> str:
        return f"Table(header={self.header}, rows={self.rows})"

    # ========== Internal Utilities ==========
    def _validate_iterable(self, value: Any, name: str) -> None:
        if isinstance(value, (str, bytes)) or not isinstance(value, Iterable):
            raise TypeError(
                f"Expected {name} to be an iterable, got {type(value).__name__}"
            )

    def _validate_string(self, value: Any, name: str) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f"Expected {name} to be a string, got {type(value).__name__}"
            )

    def _format_row(self, row: Iterable[Any]) -> str:
        return " & ".join(str(cell) for cell in row) + r" \\" + "\n"

    def _column_format(self) -> str:
        count = len(self.header) if self.header else len(self.rows[0])
        return "|" + "|".join(["c"] * count) + "|"

    def _caption(self) -> str:
        return f"\\caption{{{self.caption}}}\n" if self.caption else ""

    def _label(self) -> str:
        return f"\\label{{{self.label}}}\n" if self.label else ""

    def _build_tabular_content(self) -> str:
        all_rows = [self.header] + self.rows if self.header else self.rows
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
