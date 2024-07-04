def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '5':
            print("Saliendo...")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Por favor ingrese números válidos")
                continue

            if opcion == '1':
                resultado = sumar(num1, num2)
            elif opcion == '2':
                resultado = restar(num1, num2)
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
            elif opcion == '4':
                resultado = dividir(num1, num2)

            print(f"El resultado es: {resultado}")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
