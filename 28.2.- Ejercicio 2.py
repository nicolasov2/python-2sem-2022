# Ejercicio 2
# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución
"""
lista = [1, 2, 3, 4, 5]
lista[10]
"""

def main():
    try:
        lista = [1, 2, 3, 4, 5]
        print(lista[-1])
    except IndexError as e:
        print("El índice exece el largo total de la lista")
    

if __name__ == "__main__":
    main()