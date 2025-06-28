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
