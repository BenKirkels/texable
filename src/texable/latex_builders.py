from typing import Any, Sequence, Optional

from texable.grid import Grid
from texable.headers import Headers
from texable.line_borders import LineBorders
from texable.column_alignments import ColumnAlignments
from texable.row import Row


def make_row(row: Sequence) -> str:
    return " & ".join(str(cell) for cell in row) + r" \\" + "\n"


def make_caption(caption: str) -> str:
    return f"\\caption{{{caption}}}\n"


def make_label(label: str) -> str:
    return f"\\label{{{label}}}\n"


def make_tabular_content(
    headers: Headers, data: Grid, horizontal_borders: LineBorders
) -> str:
    latex_rows = []
    if headers.are_set:
        latex_rows.append(make_row(headers.headers))

    for row in data:
        latex_rows.append(make_row(row))

    with_borders = ""
    for i in range(len(latex_rows)):
        if horizontal_borders[i]:
            with_borders += horizontal_borders[i] + "\n"
        with_borders += latex_rows[i]
    with_borders += horizontal_borders[-1]

    return with_borders


def make_block(
    name: str,
    content: str,
    indent: str,
    required_arg: Optional[list[str]] = None,
    optional_arg: Optional[list[str]] = None,
) -> str:
    required = f"{{{', '.join(required_arg)}}}" if required_arg else ""
    optional = f"[{', '.join(optional_arg)}]" if optional_arg else ""
    indented = "\n".join(
        indent + line if line.strip() else "" for line in content.splitlines()
    )
    return f"\\begin{{{name}}}{required}{optional}\n{indented}\n\\end{{{name}}}\n"


def make_column_arg(
    vertical_borders: LineBorders, column_alignments: ColumnAlignments
) -> str:
    """Generate the column argument for the tabular environment."""
    result = ""
    for i in range(len(column_alignments)):
        result += vertical_borders[i]
        result += column_alignments[i]
    result += vertical_borders[-1]
    return result
