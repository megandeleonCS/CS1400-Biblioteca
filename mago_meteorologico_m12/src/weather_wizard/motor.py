from api import fetch_weather_from_provider
from utils import is_valid_city_name

def obtener_clima_ciudad(city_name: str):
    if not is_valid_city_name(city_name):
        raise ValueError("Nombre de ciudad no válido.")

    # Llamamos a la API
    raw_data = fetch_weather_from_provider(city_name)

    # Aquí podrías limpiar los datos antes de devolverlos
    return {
        "city": raw_data["location"]["name"],
        "temp": raw_data["current"]["temp_c"],
        "condition": raw_data["current"]["condition"]["text"]
    }