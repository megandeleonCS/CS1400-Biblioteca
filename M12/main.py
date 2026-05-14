# main.py

from utils import limpiar_y_tokenizar
from markov import construir_modelo, generar_texto

texto_original = "Hola, Megan. Nos vemos el martes. Hola, Megan. Nos vemos pronto."

palabras = limpiar_y_tokenizar(texto_original)
print("Tokens:")
print(palabras)

modelo = construir_modelo(palabras)
print("\nModelo de Markov:")
print(modelo)

texto_generado = generar_texto(modelo, "hola", 6)
print("\nTexto generado:")
print(texto_generado)