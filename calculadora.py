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


def calculadora():
    print("=== CALCULADORA BASICA ===")

    while True:
        print("\n1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("Hasta luego.")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción inválida.")
            continue

        try:
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
        else:
            resultado = dividir(a, b)

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    calculadora()