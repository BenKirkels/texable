from texable import Table


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
    table.alignments[0, 2] = ["l", "r"]

    expected_output = (
        "\\begin{table}\n"
        "  \\centering\n"
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
