from calculator.calc import Calc


def test_add():
    c = Calc(10, 15)
    assert c.add() == 25


def test_substract():
    c = Calc(25, 5)
    assert c.substract() == 20


def test_divide():
    c = Calc(15, 5)
    assert c.divide() == 3.0


def test_multiply():
    c = Calc(10, 10)
    assert c.multiply() == 100


def test_init():
    c = Calc(1, 2)
    assert c.num1 == 1
    assert c.num2 == 2
