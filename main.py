def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def x(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error"

def menu():
    print("(1): Suma\n(2): Resta\n(3): Multiplicación\n(4): Division\n(5): Salir.")

def principal():
    while True:
        menu()
        op = int(input("Ingresa la operacion a realizar: "))

        if op == 5:
            print("Saliendo")
            break

        if op in [1,2,3,4]:
            try:
                a = int(input("Dime el primer numero: "))
                b = int(input("Dime el segundo numero: "))
            except ValueError:
                print("Error.")
                continue

            if op == 1:
                result = suma(a, b)
            elif op == 2:
                result = resta(a ,b)
            elif op == 3:
                result = x(a, b)
            elif op == 4:
                result = div(a, b)

            print(f"Este es tu resultado: {result} ")
        else:
            print("Debes selecionar una de las 5 opciones.")

if __name__ == "__main__":
    principal()
