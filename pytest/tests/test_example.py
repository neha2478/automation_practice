# def test_pass():
#     assert 1 + 1 == 2

# def test_fail():
#     assert 2 + 2 == 5


def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    # assert 5 * 5 == 35
    assert 5 / 5 == 1


def test_equality():
    assert 1 + 2 == 3

def test_membership():
    assert "a" in "abcd"

def test_bool():
    assert True
    assert not False

def test_list():
    assert [1, 2, 3, 4] == [2, 3, 4, 1]
    assert [1, 2, 3] == [1, 2, 3]


#here we are using Exception handling
'''
import pytest

def test_expectation():
    with pytest.raises(ZeroDivisionError):
        1 / 0
'''

def test_a2():
    assert 7/3 == 2.3 #here the message that will be print if failed

def test_a4():
    assert 9//5 == 1 #integer division

