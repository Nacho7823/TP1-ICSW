from calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0


def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5


def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-2, 3) == -6


def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(5, 2) == 2.5


def test_dividir_por_cero():
    assert dividir(5, 0) == "Error: no se puede dividir por cero"
