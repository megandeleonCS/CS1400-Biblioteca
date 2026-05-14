"""
Funciones de utilidad para Weather Wizard.
Contiene herramientas de conversión y formateo de texto.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convierte una temperatura de grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


def formatear_respuesta(data: dict) -> str:
    """
    Toma un diccionario de datos climáticos y lo devuelve como
    una cadena de texto elegante para la consola.
    """
    city = data.get("city", "Desconocida").capitalize()
    temp = data.get("temp", 0)
    condition = data.get("condition", "N/A").upper()

    temp_f = celsius_to_fahrenheit(temp)

    report = [
        f"REPORTE CLIMATICO PARA: {city}",
        f"{'-'*30}",
        f"Temperatura: {temp} C ({temp_f:.1f} F)",
        f"Condicion:   {condition}",
        f"{'-'*30}"
    ]

    return "\n".join(report)


def is_valid_city_name(name: str) -> bool:
    """Verifica si el nombre de la ciudad tiene al menos 2 letras."""
    return isinstance(name, str) and len(name.strip()) >= 2