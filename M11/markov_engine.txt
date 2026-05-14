# markov.py
import random

def construir_modelo(palabras):
    """
    Crea un diccionario donde cada palabra es una clave y su valor
    es una lista de todas las palabras que la siguen.
    """
    modelo = {}
    for i in range(len(palabras) - 1):
        palabra_actual = palabras[i]
        palabra_siguiente = palabras[i + 1]

        if palabra_actual not in modelo:
            modelo[palabra_actual] = []

        modelo[palabra_actual].append(palabra_siguiente)

    return modelo


def generar_texto(modelo, palabra_inicial, longitud):
    """
    Genera una secuencia de palabras basada en las probabilidades del modelo.
    """
    frase_generada = [palabra_inicial]
    palabra_actual = palabra_inicial

    for _ in range(longitud - 1):
        if palabra_actual in modelo:
            siguiente = random.choice(modelo[palabra_actual])
            frase_generada.append(siguiente)
            palabra_actual = siguiente
        else:
            break

    return " ".join(frase_generada)