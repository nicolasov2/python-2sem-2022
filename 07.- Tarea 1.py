# Tarea 1: Crear un conversor de moneda para transformar a dólares USD, de distintas monedas. 1) Peso Chileno 2) Peso Argentino 3) Peso Mexicano

bienvenida = """
Bienvenido al conversor de moneda

1) Peso Chileno
2) Peso Argentino
3) Peso Mexicano

Elija una opción: """

opcion = int(input(bienvenida))

if opcion == 1:
    # Convertir de CLP a USD
    pesos = int(input("Ingrese pesos CLP: "))
    valor_dolar = 925
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(str(dolares)  + " dolares")
elif opcion == 2:
    # Convertir de CLP a USD
    pesos = int(input("Ingrese pesos ARG: "))
    valor_dolar = 144
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(str(dolares)  + " dolares")
elif opcion == 3:
    # Convertir de CLP a USD
    pesos = int(input("Ingrese pesos MX: "))
    valor_dolar = 20
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(str(dolares)  + " dolares")
else:
    print("Opción no válida")