from texable import Table
from texable.custom_types import Alignment


def test_example1():
    table = Table(
        [
            [1, 2, 0],
            [3, 4, 0],
            [5, 6, 0],
        ]
    )

    table.headers = ("Column 1", "Column 2", "Column 3")
    table.caption = "This is a sample table caption."
    table.label = "tab:sample_table"
    table.column_alignments[0, 2] = [Alignment.LEFT, Alignment.RIGHT]
    table.table_alignment = Alignment.RIGHT

    expected_output = (
        "\\begin{table}\n"
        "  \\raggedright\n"
        "  \\begin{tabular}{lcr}\n"
        "    Column 1 & Column 2 & Column 3 \\\\\n"
        "    1 & 2 & 0 \\\\\n"
        "    3 & 4 & 0 \\\\\n"
        "    5 & 6 & 0 \\\\\n"
        "  \\end{tabular}\n"
        "  \\caption{This is a sample table caption.}\n"
        "  \\label{tab:sample_table}\n"
        "\\end{table}\n"
    )

    assert str(table) == expected_output
