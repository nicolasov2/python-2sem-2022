# Función anónima o lambda

# Las funciones lambda son funciones que se definen en una sola linea
# Se usan para definir funciones simples que no requieren un nombre y solo se usaran 1 vez
# Se usan en conjunto con otras funciones como: map, filter y reduce
# Forma: lambda a, b: a + b

def main():
    # Función anónima que suma dos numeros
    suma = lambda a, b: a + b
    print( suma(2, 3) )

    # Función anónima con condicional
    # lambda argumentos: expresion if condicion else expresion
    suma = lambda a, b: a + b if a > 0 else a - b
    print(suma(0, 3))

    print( doblar_tradicional(2) )
    print( doblar_simplificado(3) )

    # Forma con lambda
    doblar_lambda = lambda numero: numero * 2
    print( doblar_lambda(4) )

# Ejemplo: Doblar un numero
# Forma tradicional
def doblar_tradicional(numero):
    resultado = numero * 2
    return resultado

# Forma simplificada
def doblar_simplificado(numero):
    return numero * 2


if __name__ == '__main__':
    main()