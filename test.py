from textmathsolve import TextMathSolver
import pytest
from pytest import approx


@pytest.mark.parametrize("inputs,expected", [
    ("1+1", 2.0),
    ("1.1-3.2", -2.1),
    ("6.4/1.6", approx(4)),
])
def test_TextMathSolver(inputs, expected):
    solver = TextMathSolver()
    assert solver(inputs) == expected