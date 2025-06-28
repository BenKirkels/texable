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
    assert table.to_latex() == expected_output


def test_example2():
    table = Table(
        [
            ["cell 1", "cell 2", "cell 3"],
            ["cell 4", "cell 5", "cell 6"],
            ["cell 7", "cell 8", "cell 9"],
        ]
    )

    table.horizontal_borders.outer()
    table.vertical_borders.all()

    expected_output = (
        "\\begin{table}\n"
        "  \\centering\n"
        "  \\begin{tabular}{|c|c|c|}\n"
        "    \\hline\n"
        "    cell 1 & cell 2 & cell 3 \\\\\n"
        "    cell 4 & cell 5 & cell 6 \\\\\n"
        "    cell 7 & cell 8 & cell 9 \\\\\n"
        "    \\hline\n"
        "  \\end{tabular}\n"
        "\\end{table}\n"
    )
    assert table.to_latex() == expected_output


def test_example3():
    table = Table(
        [
            [1, 6, 87837, 787],
            [2, 7, 78, 5415],
            [3, 545, 778, 7507],
            [4, 545, 18744, 7560],
            [5, 88, 788, 6344],
        ]
    )
    table.headers = ("Col1", "Col2", "Col2", "Col3")

    table.horizontal_borders.all("single")
    table.horizontal_borders.at(1, "double")
    table.vertical_borders.outer("double")

    expected_output = (
        "\\begin{table}\n"
        "  \\centering\n"
        "  \\begin{tabular}{||cccc||}\n"
        "    \\hline\n"
        "    Col1 & Col2 & Col2 & Col3 \\\\\n"
        "    \\hline\\hline\n"
        "    1 & 6 & 87837 & 787 \\\\\n"
        "    \\hline\n"
        "    2 & 7 & 78 & 5415 \\\\\n"
        "    \\hline\n"
        "    3 & 545 & 778 & 7507 \\\\\n"
        "    \\hline\n"
        "    4 & 545 & 18744 & 7560 \\\\\n"
        "    \\hline\n"
        "    5 & 88 & 788 & 6344 \\\\\n"
        "    \\hline\n"
        "  \\end{tabular}\n"
        "\\end{table}\n"
    )
    assert table.to_latex() == expected_output
