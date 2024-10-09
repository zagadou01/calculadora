def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def modulo(a, b):
    return a % b

def promedio(a, b):
    return (a + b) / 2

def inicio():
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    
    print("Elija una opción de la calculadora: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Promedio")
    print("7. Salir")

    opcion = int(input("Opción: "))
    
    if opcion == 7:
        return
    elif opcion == 1:
        print(suma(a, b))
    elif opcion == 2:
        print(resta(a, b))
    elif opcion == 3:
        print(multiplicacion(a, b))
    elif opcion == 4:
        print(division(a, b))
    elif opcion == 5:
        print(modulo(a, b))
    elif opcion == 6:
        print(promedio(a, b))
    else:
        print("Opción no válida")

inicio()