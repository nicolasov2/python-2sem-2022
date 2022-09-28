# Bucles

def main():

    # While
    contador = 10
    while contador > 0:
        print("Hola")
        # contador = contador + 1
        contador -= 1

    # For
    palabra = "Supercalifragilisticoespialidoso"
    for letra in palabra:
        print(letra)

    lista = range(1000)
    for l in lista:
        if l == 5:
            continue
        
        print(l)
        
        if l == 10:
            break


if __name__ == "__main__":
    main()
