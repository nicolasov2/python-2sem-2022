# *args y **kwargs

# args y kwargs pueden lllevar cualquier nombre pero es una convención usarlos así
# lo importante son * y **
# se usan para pasar un numero variable de parametros a una función

# *args -> arguments | es una tupla (elemnto1, elemnto2, elemnto3)
# **kwargs -> key word arguments | es un diccionario {'elemnto1': valor, 'elmento2': valor}

# *args
# Argumentos queno estan asociados a un nombre
def prueba_args(argumento, *args):
    print(argumento)
    for arg in args:
        print(arg)

prueba_args("Hola", "Mundo", ["Python", "PHP", "JAVA"], 4.5, 3, True)

# **kwargs
# Argumentos que si estan asociados a un nombre
def prueba_kwargs(**kwargs):
    for key, value in kwargs.items():
        # print(key)
        # print(value)
        print("{0}: {1}".format(key, value))

prueba_kwargs(nombre="Juan", apellido="Perez", edad=25)

kwargs_diccionario = {
    "arg1": 1, 
    "arg2": "DOS", 
    "arg3": 4.5
}
prueba_kwargs(**kwargs_diccionario)

# Ejemplo: Función que sume todos los valores que le envíe por parametros y devuelva el resultado
def suma(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total

resultado_suma = suma(1,2,3,4,5,6,7,8,9,10)
print(resultado_suma)

# Ejercicio: 
# Función que recipa la operación a realizar y los numeros a operar y devuelva el resultado

def calculadora(operacion, *args):
    if operacion == 'suma':
        total = 0
        for arg in args:
            total += arg
        return total
    elif operacion == 'resta':
        total = 0
        for arg in args:
            total -= arg
        return total
    elif operacion == 'multiplicacion':
        total = 1
        for arg in args:
            total *= arg
        return total
    elif operacion == 'division':
        total = 1
        for arg in args:
            total /= arg
        return total
    else:
        return "Operación no válida"

resultado = calculadora('division', 3, 2, 5)
print(resultado)