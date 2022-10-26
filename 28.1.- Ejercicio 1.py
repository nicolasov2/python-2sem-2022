# Ejercicio 1
# Cree una función que divida dos números y los retorne. La función debe ser capaz de enviar un mensaje si se ingresa un valór no válido o matematicamente imposible, en el caso de haber error devolver un numero 0

def division(num_1, num_2):
    try:
        resultado = num_1 / num_2
    except ZeroDivisionError:
        print("Error, división por 0")
        resultado = 0
    except Exception as e:
        print("Ocurrio un error: ")
        print(e)
        resultado = 0
    finally:
        return resultado

def main():
    try:
        print(division(1, 0))
    except Exception as e:
        print(e)

    
if __name__ == "__main__":
    main()