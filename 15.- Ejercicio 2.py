# Ejercicio 2: Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

def area_circulo(radio):
    pi = 3.1415
    area = pi * (radio ** 2)
    return area

def volumen_cilindro(radio, altura):
    circulo = area_circulo(radio)
    volumen = circulo * altura
    return volumen

def main():
    a_circulo = area_circulo(3)
    v_cilindro = volumen_cilindro(3, 7)

    print(a_circulo)
    print(v_cilindro)

if __name__ == '__main__':
    main()