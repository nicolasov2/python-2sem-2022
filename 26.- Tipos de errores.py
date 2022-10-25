# Errores de sintaxis
# print("Hola"))

# Error división entre 0
# print( 0 / 0 )

# Error variable no definida
# print(suma)

# Error assertion
suma = lambda x, y: x + y
assert suma(1, 2) == 3
# assert: comprueba que la condición es verdadera, si no lo es genera un error

# Generar una excepción
edad = 21
if edad < 18:
    raise Exception("El usuario es menor de edad")

