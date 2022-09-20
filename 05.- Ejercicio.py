# numero = input("Ingrese un número: ")
# print(numero)

# Ejercicio: Programa que reciba una cantidad de pesos y los transforme a dólar
pesos = int(input("Ingrese pesos CLP: "))
valor_dolar = 925
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
print(str(dolares)  + " dolares")