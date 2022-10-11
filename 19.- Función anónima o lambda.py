# Función anónima o lambda

# Las funciones lambda son funciones que se definen en una sola linea
# Se usan para definir funciones simples que no requieren un nombre y solo se usaran 1 vez
# Se usan en conjunto con otras funciones como: map, filter y reduce
# Forma: lambda a, b: a + b

def main():
    # Función anónima que suma dos numeros
    suma = lambda a, b: a + b
    print( suma(2, 3) )

if __name__ == '__main__':
    main()