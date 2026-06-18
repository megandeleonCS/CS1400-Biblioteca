# main.py
from utils import limpiar_y_tokenizar
from markov import construir_modelo, generar_texto

def ejecutar_demo():
    # 1. Datos de entrada
    texto_base = "Allí estaban, las figuras animatrónicas, sus ojos de plata fijos en la oscuridad, inmóviles y amenazantes."
    
    # 2. Procesamiento (Usando utils.py)
    palabras = limpiar_y_tokenizar(texto_base)
    
    # 3. Construcción (Usando markov_engine.py)
    modelo = construir_modelo(palabras)
    
    # 4. Generación
    print("--- Generador de Texto Markov ---")
    resultado = generar_texto(modelo, "allí", 5)
    
    print(f"Resultado: {resultado}")

# TODO Paso 6.
# Llama a ejecutar_demo() dentro de un bloque if __name__ == "__main__":
if __name__ == "__main__":
    ejecutar_demo()