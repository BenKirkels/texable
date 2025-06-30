from typing import Callable
from texable.packages import require_package


def bold(text: str) -> str:
    """
    Formats the given text in bold LaTeX format.

    Args:
        text (str): The text to format.

    Returns:
        str: The formatted text in bold.
    """
    return f"\\textbf{{{text}}}"


def italic(text: str) -> str:
    """
    Formats the given text in italic LaTeX format.
    Args:
        text (str): The text to format.
    Returns:
        str: The formatted text in italic.
    """
    return f"\\textit{{{text}}}"


def text_color(color_name: str) -> Callable[[str], str]:
    """
    Creates a formatter that applies the specified color to the text.

    Args:
        color_name (str): The name of the color to apply.

    Returns:
        Callable[[str], str]: A function that formats text in the specified color.
    """

    def formatter(text: str) -> str:
        require_package("xcolor")
        return f"\\textcolor{{{color_name}}}{{{text}}}"

    return formatter


def cell_color(color_name: str) -> Callable[[str], str]:
    """
    Creates a formatter that applies the specified color to the cell content.

    Args:
        color_name (str): The name of the color to apply.

    Returns:
        Callable[[str], str]: A function that formats cell content in the specified color.
    """

    def formatter(text: str) -> str:
        require_package("xcolor", ["table"])
        return f"\\cellcolor{{{color_name}}}{{{text}}}"

    return formatter
