# Map

# Aplica una a cada elemento de una lista
# map(funcion, lista)

def main():
    # Ejemplo: convertir una lista de numeros a una lista con sus cuadrados
    
    # Forma tradicional
    lista = [1, 2, 3, 4, 5]
    al_cuadrado = []
    for numero in lista:
        al_cuadrado.append(numero ** 2)
    print(al_cuadrado)

    # Forma con map
    lista = [1, 2, 3, 4, 5]
    al_cuadrado = list( map(lambda numero: numero ** 2, lista) )
    print(al_cuadrado)

if __name__ == '__main__':
    main()