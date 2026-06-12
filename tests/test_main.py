from src.main import add

def test_add_1():
    assert add(1, 2) == 3

def test_add_2():
    assert add(1, 2, 3) == 6

def test_add_3():
    assert add("1", "2") == 3

def test_add_error():
    assert add("a", 1) == "error"
