from src.neis import getOvertime


def testerGetOvertime():
    assert getOvertime(16, 50, 21, 50) == (5, 0), "Should be (5, 0)"
    assert getOvertime(7, 52, 8, 50) == (0, 58), "Should be (0, 58)"
    assert getOvertime(16, 50, 16, 50) == (0, 0), "Should be (0, 0)"
    assert getOvertime(12, 40, 17, 10) == (4, 30), "Should be (4, 30)"
    assert getOvertime(12, 37, 15, 31) == (2, 54), "Should be (3, 30)"


testerGetOvertime()