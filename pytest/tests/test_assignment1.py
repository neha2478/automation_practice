
#Assignment 1

def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def fun(x):
    return x + 2

def test_answer():
    assert fun(3) == 6