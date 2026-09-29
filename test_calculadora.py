from calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada


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


def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(2, -1) == 0.5


def test_raiz_cuadrada():
    assert raiz_cuadrada(9) == 3
    assert raiz_cuadrada(0) == 0
    assert raiz_cuadrada(-1) == "Error: no se puede calcular la raíz de un número negativo"

