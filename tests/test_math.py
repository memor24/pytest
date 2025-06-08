import pytest

def test_pass_example():
    assert 2+2 == 4

def test_fail_example():
    a=2
    b=2
    c=5
    assert a+b == c

def test_error_example():
    with pytest.raises(ZeroDivisionError) as e:
        num=1/0
        
    assert str(e.value) == "division by zero"