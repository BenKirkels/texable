from texable import Table


def test_default_no_headers():
    """Test that a table without headers has no headers set."""
    table = Table(3)

    assert not any(table.headers)
    assert table.headers.are_set is False


def test_set_headers():
    """Test setting headers for a table."""
    table = Table(3)
    headers = ["Header 1", "Header 2", "Header 3"]
    table.headers = headers

    assert all(h1 == h2 for h1, h2 in zip(table.headers, headers))
    assert table.headers.are_set is True


def test_set_single_header():
    """Test setting a single header."""
    table = Table(3)
    table.headers[0] = "Header 1"

    assert table.headers[0] == "Header 1"
    assert table.headers[1] == ""  # Remaining headers should be empty
    assert table.headers[2] == ""
    assert table.headers.are_set is True


def test_set_multiple_headers():
    """Test setting multiple headers at once."""
    table = Table(3)
    table.headers[0:2] = ["Header 1", "Header 2"]

    assert table.headers[0] == "Header 1"
    assert table.headers[1] == "Header 2"
    assert table.headers[2] == ""  # Last header should remain empty
    assert table.headers.are_set is True


def test_set_combined_headers():
    """Test setting a combination of individual and multiple headers."""
    table = Table(3)
    table.headers[0, 2] = ["Header 1", "Header 3"]

    assert table.headers[0] == "Header 1"
    assert table.headers[1] == ""  # Middle header should remain empty
    assert table.headers[2] == "Header 3"
    assert table.headers.are_set is True


def test_set_headers_with_invalid_type():
    """Test setting headers with an invalid type."""
    table = Table(3)
    try:
        table.headers[0] = 123  # type: ignore # Invalid type
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError when setting header with invalid type"


def test_set_headers_with_invalid_length():
    """Test setting headers with an invalid length."""
    table = Table(3)
    try:
        table.headers[0:2] = ["Header 1"]  # Only one header provided
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when setting headers with mismatched length"


def test_set_headers_with_invalid_index():
    """Test setting headers with an index out of range."""
    table = Table(3)
    try:
        table.headers[3] = "Header 4"  # Index out of range
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError when setting header with out-of-range index"


def test_support_tuple_value():
    """Test setting headers using a tuple."""
    table = Table(3)
    table.headers[0, 1] = ("Header 1", "Header 2")

    assert table.headers[0] == "Header 1"
    assert table.headers[1] == "Header 2"
    assert table.headers[2] == ""  # Last header should remain empty
    assert table.headers.are_set is True
