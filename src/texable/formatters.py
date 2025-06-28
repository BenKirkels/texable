from typing import Callable


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


def color(color_name: str) -> Callable[[str], str]:
    """
    Creates a formatter that applies the specified color to the text.

    Args:
        color_name (str): The name of the color to apply.

    Returns:
        Callable[[str], str]: A function that formats text in the specified color.
    """

    def formatter(text: str) -> str:
        return f"\\textcolor{{{color_name}}}{{{text}}}"

    return formatter
