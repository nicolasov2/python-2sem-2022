# Evitar que nuestro código se detenga cuando hay un error

# try:
#     print(0 / 0)
# except ZeroDivisionError as error:
#     print("Error, se está tratando de dividir entre 0")
#     print(error)

# print("Hola mundo")

# try:
#     assert 1 != 1
# except AssertionError as error:
#     print(error)

# try:
#     edad = 17
#     if edad < 18:
#         raise Exception("El usuario es menor de edad")
# except Exception as error:
#     print(error)

# Simplificando codigo
try: 
    print(1 / 2)
    assert 1 == 1
    edad = 21
    if edad < 18:
        raise Exception("El usuario es menor de edad")
    
    print("hola")
except ZeroDivisionError as error:
    print("Error, se está tratando de dividir entre 0")
    print(error)
except AssertionError as error:
    print("Assertion Error")
    print(error)
except Exception as error:
    print(error)
else:
    print("El usuario debe se mayor de edad para ingresar")
finally:
    print("El programa terminó")



"""

try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
    
except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error
    
else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
   
finally:
	# Este bloque se ejecutara siempre
"""