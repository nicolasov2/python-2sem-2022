# Listas

def main():
    numeros = [1,2,3,4,5,6]
    print( type(numeros) )

    print(numeros[1])

    lista_objetos = [5, "Hola", 3.5, True, [2,3]]
    print( type(lista_objetos) )

    # Agregar un elementos
    lista_objetos.append("Marcha")

    # Eliminar elementos
    lista_objetos.pop(1)

    for elementos in lista_objetos[::-1]:
        print( elementos )

    nueva_lista = []
    print(nueva_lista)
    for numero in range(10):
        nueva_lista.append(numero)

    print(nueva_lista)

    suma_listas = lista_objetos + nueva_lista
    print(suma_listas)

if __name__ == "__main__":
    main()