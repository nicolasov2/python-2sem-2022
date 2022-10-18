# Filter

# Filtrar los elementos de una lista que cumplan una condicion
# Similar a un bucle for con condicional, pero más eficiente


def main():
    # Filtrar los numeros menores que cero
    lista = range(-5, 5)
    menor_cero = list( filter(lambda numero: numero < 0, lista) )
    print(menor_cero)

if __name__ == '__main__':
    main()