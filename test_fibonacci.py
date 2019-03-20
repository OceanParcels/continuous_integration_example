from fibonacci import fibonacci, strict_fibonacci
import pytest


@pytest.mark.parametrize('n', [0, 1, 5, -1])
def test_fibonacci(n):
    f = fibonacci(n)
    assert(type(f) == int and f >= 0), \
        'Fibonacci sequence should return a positive integer'


@pytest.mark.parametrize(
        'n', [1, pytest.param(-1, marks=pytest.mark.xfail(strict=True))])
def test_strict_fibonacci(n):
    f = strict_fibonacci(n)
    assert (type(f) == int and f >= 0), \
        'Fibonacci sequence should return a positive integer'
