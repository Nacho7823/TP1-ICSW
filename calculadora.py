def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no es posible realizar una division por 0"
    return a / b


def potencia(a, b):
    return a ** b


def raiz_cuadrada(a):
    if a < 0:
        return "Error: no se puede calcular la raíz de un número negativo"
    return a ** 0.5


def calculadora():
    print("=== CALCULADORA BASICA ===")

    while True:
        print("\n1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "7":
            print("Hasta luego.")
            break

        if opcion not in ("1", "2", "3", "4", "5", "6"):
            print("Opción inválida.")
            continue

        try:
            if opcion == "6":
                a = float(input("Ingrese el número: "))
                resultado = raiz_cuadrada(a)
                print(f"Resultado: {resultado}")
                continue
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: ingrese números válidos.")
            continue

        if opcion == "1":
            resultado = sumar(a, b)
        elif opcion == "2":
            resultado = restar(a, b)
        elif opcion == "3":
            resultado = multiplicar(a, b)
        elif opcion == "4":
            resultado = dividir(a, b)
        else:
            resultado = potencia(a, b)

        print(f"\nResultado:\n{resultado}")


if __name__ == "__main__":
    calculadora()