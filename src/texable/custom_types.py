from enum import Enum


class Alignment(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2

    def column(self) -> str:
        """Return the LaTeX column alignment character for this alignment."""
        match self:
            case Alignment.LEFT:
                return "l"
            case Alignment.CENTER:
                return "c"
            case Alignment.RIGHT:
                return "r"
            case _:
                raise ValueError("Invalid alignment type.")

    def table(self) -> str:
        """Return the LaTeX table alignment command for this alignment."""
        match self:
            case Alignment.LEFT:
                return "\\raggedleft"
            case Alignment.CENTER:
                return "\\centering"
            case Alignment.RIGHT:
                return "\\raggedright"
            case _:
                raise ValueError("Invalid alignment type.")
