from texable import Table


def test_default_alignment():
    """Test the default alignment of a table."""
    table = Table(3)
    assert table.alignments[0] == "c"
    assert table.alignments[1] == "c"
    assert table.alignments[2] == "c"

    assert len(table.alignments) == 3


def test_individual_alignment():
    """Test setting an individual column alignment."""
    table = Table(3)
    table.alignments[0] = "l"

    assert table.alignments[0] == "l"
    assert table.alignments[1] == "c"
    assert table.alignments[2] == "c"


def test_slice_alignment():
    """Test setting multiple column alignments using a slice."""
    table = Table(3)
    table.alignments[1:3] = ["r", "l"]

    assert table.alignments[0] == "c"
    assert table.alignments[1] == "r"
    assert table.alignments[2] == "l"


def test_combined_alignment():
    """Test setting a combination of individual alignments"""
    table = Table(3)
    table.alignments[0, 2] = "l"

    assert table.alignments[0] == "l"
    assert table.alignments[1] == "c"
    assert table.alignments[2] == "l"


def test_full_alignment():
    """Test setting all column alignments at once."""
    table = Table(3)
    table.alignments = ["l", "c", "r"]

    assert table.alignments[0] == "l"
    assert table.alignments[1] == "c"
    assert table.alignments[2] == "r"


def test_invalid_alignment_type():
    """Test setting an invalid alignment type."""
    table = Table(3)
    try:
        table.alignments[0] = 1  # type: ignore # Invalid type
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError not raised."


def test_invalid_alignment_value():
    """Test setting an invalid alignment value."""
    table = Table(3)
    try:
        table.alignments[0] = "x"  # Invalid alignment
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised."


def test_index_out_of_range():
    """Test accessing an alignment index that is out of range."""
    table = Table(3)
    try:
        _ = table.alignments[3]  # Out of range
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError not raised."

    try:
        table.alignments[5] = "l"  # Out of range
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError not raised."


def test_support_tuple_value():
    """Test setting alignments using a tuple."""
    table = Table(3)
    table.alignments[0, 2] = ("l", "r")

    assert table.alignments[0] == "l"
    assert table.alignments[1] == "c"
    assert table.alignments[2] == "r"
