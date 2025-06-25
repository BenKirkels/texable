# https://www.overleaf.com/learn/latex/Tables
from texable.table import Table


def test_example1():
    table = Table(
        [
            ["cell 1", "cell 2", "cell 3"],
            ["cell 4", "cell 5", "cell 6"],
            ["cell 7", "cell 8", "cell 9"],
        ]
    )

    expected_output = (
        "\\begin{table}\n"
        "  \\centering\n"
        "  \\begin{tabular}{ccc}\n"
        "    cell 1 & cell 2 & cell 3 \\\\\n"
        "    cell 4 & cell 5 & cell 6 \\\\\n"
        "    cell 7 & cell 8 & cell 9 \\\\\n"
        "  \\end{tabular}\n"
        "\\end{table}\n"
    )
    assert str(table) == expected_output
