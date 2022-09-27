# Palíndromos

# Luz Azul
# Ana
# Yo hago Yoga hoy
# Anita lava la tina

# Escribir un programa que identifique si una palabra es palíndromo o no

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

palabra = palindromo(input("Ingrese frase: "))
if palabra:
    print("Si es un palindromo")
else:
    print("No es palindormo")