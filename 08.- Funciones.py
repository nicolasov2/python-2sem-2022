# Funciones

def holaMundo():
    print("Hola mundo desde una función")

# holaMundo()

# Refactorizando Convertidor de moneda
def conversor_moneda(moneda, valor_dolar = 900):
    pesos = int(input("Ingrese pesos " + moneda + ": "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(str(dolares)  + " dolares")

bienvenida = """
Bienvenido al conversor de moneda

1) Peso Chileno
2) Peso Argentino
3) Peso Mexicano

Elija una opción: """

opcion = int(input(bienvenida))

if opcion == 1:
    # Convertir de CLP a USD
    conversor_moneda("CLP", 925)
elif opcion == 2:
    # Convertir de ARG a USD
    conversor_moneda("ARG", 144)
elif opcion == 3:
    # Convertir de MX a USD
    conversor_moneda("MX", 20)
else:
    print("Opción no válida")