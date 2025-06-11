from typing import Any, Sequence, Optional

from texable.headers import Headers


def make_row(row: Sequence[Any]) -> str:
    return " & ".join(str(cell) for cell in row) + r" \\" + "\n"


def make_caption(caption: str) -> str:
    return f"\\caption{{{caption}}}\n"


def make_label(label: str) -> str:
    return f"\\label{{{label}}}\n"


def make_tabular_content(headers: Headers, rows: list[list[str]]) -> str:
    all_rows = [headers.headers] + rows if headers.are_set else rows
    return "".join(make_row(row) for row in all_rows)


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
