# Utilizar la función map() para crear una función que retorne una lista con la longitud de cada palabra (separas por espacios) de una frase. La función recibe una cadena de texto y retornara una lista.

def longitud_palabra(texto):
    lista_texto = texto.split()
    largo_palabra = list( map(len, lista_texto) )
    return largo_palabra


def main():
    resultado = longitud_palabra("Hola mundo, desde Python")
    print(resultado)

if __name__ == '__main__':
    main()