import pytest
from texable.cell import Cell  # Replace with the correct path if needed


def uppercase(s: str) -> str:
    return s.upper()


def wrap_bold(s: str) -> str:
    return f"\\textbf{{{s}}}"


def test_initialization_and_value():
    c = Cell(42)
    assert c.value == 42

    c.value = 100
    assert c.value == 100


def test_str_and_repr():
    c = Cell("hello")
    assert str(c) == "hello"
    assert repr(c) == "Cell(hello)"


def test_add_formatters_and_to_latex():
    c = Cell("text")
    c.add_formatters(uppercase, wrap_bold)

    result = c.to_latex()
    assert result == "\\textbf{TEXT}"


def test_to_latex_without_formatters():
    c = Cell("plain")
    assert c.to_latex() == "plain"


def test_equality_and_comparison():
    c1 = Cell(5)
    c2 = Cell(5)
    c3 = Cell(10)

    assert c1 == c2
    assert c1 != c3
    assert c1 < c3
    assert c3 > c2

    # Comparisons with raw values
    assert c1 == 5
    assert c1 < 6
    assert c1 > 4


def test_comparison_with_incompatible_type():
    c = Cell("hello")
    assert (c == object()) is False

    with pytest.raises(TypeError):
        _ = c < object()
