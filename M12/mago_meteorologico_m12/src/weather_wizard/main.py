"""
Punto de entrada para la aplicación Weather Wizard.
Organizado para la clase CS1400 - Universidad Weber.
"""

try:
    from weather_wizard.motor import obtener_clima_ciudad
except ModuleNotFoundError:
    from motor import obtener_clima_ciudad


def main():
    print("--- Bienvenido a Weather Wizard ---")

    ciudad = input("Introduce una ciudad (ej. London): ").strip()

    if not ciudad:
        print("Error: No ingresaste ninguna ciudad.")
        return

    try:
        resultado = obtener_clima_ciudad(ciudad)

        if not isinstance(resultado, dict):
            print("Ocurrió un error: respuesta inválida.")
            return

        if "error" in resultado:
            print(f"Ocurrió un error: {resultado['error']}")
            return

        ciudad_res = resultado.get("city", "N/A")
        temp = resultado.get("temp", "N/A")
        condicion = resultado.get("condition", "N/A")

        print(f"\nClima en: {ciudad_res}")
        print(f"Temperatura: {temp}°C")
        print(f"Condición: {condicion}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()