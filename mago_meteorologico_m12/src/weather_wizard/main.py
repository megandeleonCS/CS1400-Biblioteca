"""
Punto de entrada para la aplicación Weather Wizard.
Este archivo coordina la interfaz de usuario con el motor de lógica.
"""
import sys
from motor import obtener_clima_ciudad
from utils import formatear_respuesta

def main():
    """Función que organiza el flujo de ejecución."""
    print("--- Bienvenido a Weather Wizard API ---")
    
    # 1. Entrada de datos
    ciudad = input("Ingresa el nombre de la ciudad: ").strip()
    
    if not ciudad:
        print("Error: No ingresaste una ciudad válida.")
        sys.exit(1)

    # 2. Llamada a la lógica (Motor)
    try:
        datos_crudos = obtener_clima_ciudad(ciudad)
        
        # 3. Procesamiento/Formateo
        mensaje_final = formatear_respuesta(datos_crudos)
        
        # 4. Salida
        print(f"\nResultado: {mensaje_final}")
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Este bloque asegura que el código solo se ejecute si corres este archivo directamente,
# y no si alguien lo importa como librería.
if __name__ == "__main__":
    main()