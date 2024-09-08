from textmathsolve import TextMathSolver
import pytest


@pytest.mark.parametrize("inputs,expected", [
    ("1+1", 2.0),
    ("1.1-3.2", -2.1),
    ("6/2", 3.0),
])
def test_TextMathSolver(inputs, expected):
    solver = TextMathSolver()
    assert solver(inputs) == expected