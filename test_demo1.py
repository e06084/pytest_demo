import pytest

# pytest -s -v demo1.py
# pytest -s -v -k func1 demo1.py
# pytest -s -v demo1.py::test_func1

def test_func1():
    assert 1 == 1

def test_func2():
    assert 1 != 1

