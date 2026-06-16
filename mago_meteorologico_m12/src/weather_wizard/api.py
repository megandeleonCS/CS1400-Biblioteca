"""
Módulo para manejar las comunicaciones externas.
Este archivo se encarga de conectar con servidores de clima reales.
"""

import requests
import os 
from dotenv import load_dotenv

# En un entorno profesional, esto vendría de un archivo .env
load_dotenv()
BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("WEATHER_API_KEY")  # Solo para propósitos educativos

def fetch_weather_from_provider(city_name: str) -> dict:
    """
    Realiza una petición HTTP GET para obtener el clima de una ciudad.
    
    Retorna:
        dict: Los datos en formato JSON si la petición es exitosa.
    Lanza:
        ConnectionError: Si el servidor no responde.
        ValueError: Si la ciudad no existe.
    """
    parametros = {
        "key": API_KEY,
        "q": city_name,
        "lang": "es"
    }

    try:
        respuesta = requests.get(BASE_URL, params=parametros, timeout=10)
        
        # Si la respuesta es 404 o 500, esto lanza una excepción
        respuesta.raise_for_status()
        
        return respuesta.json()

    except requests.exceptions.HTTPError:
        raise ValueError(f"No pudimos encontrar la ciudad: {city_name}")
    except requests.exceptions.RequestException:
        raise ConnectionError("Error de red: No se pudo conectar con el servidor de clima.")