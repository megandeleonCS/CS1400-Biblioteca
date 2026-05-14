try:
    from weather_wizard.api import fetch_weather_from_provider
except ModuleNotFoundError:
    from api import fetch_weather_from_provider


def obtener_clima_ciudad(nombre_ciudad: str) -> dict:
    """
    Obtiene el clima de una ciudad usando la API
    y devuelve solo los datos necesarios para mostrar.
    """
    try:
        if not nombre_ciudad or not isinstance(nombre_ciudad, str):
            return {"error": "Nombre de ciudad no válido."}

        datos = fetch_weather_from_provider(nombre_ciudad.strip())

        if not isinstance(datos, dict):
            return {"error": "Respuesta inválida de la API."}

        if datos.get("error"):
            return {"error": datos["error"]}

        location = datos.get("location") or {}
        current = datos.get("current") or {}
        condition = current.get("condition") or {}

        return {
            "city": location.get("name", "Desconocida"),
            "temp": current.get("temp_c", 0),
            "condition": condition.get("text", "N/A")
        }

    except Exception as e:
        return {"error": f"Error inesperado: {e}"}