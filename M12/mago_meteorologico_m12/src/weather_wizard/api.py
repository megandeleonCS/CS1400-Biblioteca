import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"


def cargar_env():
    """
    Lee el archivo .env manualmente y carga las variables en el entorno.
    """
    if not os.path.exists(".env"):
        return

    with open(".env") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea and not linea.startswith("#"):
                clave, valor = linea.split("=", 1)
                os.environ[clave.strip()] = valor.strip()


# Cargar variables antes de usarlas
cargar_env()

API_KEY = os.getenv("WEATHER_API_KEY")


def fetch_weather_from_provider(city_name: str) -> dict:
    """
    Llama a WeatherAPI y devuelve los datos en formato JSON.
    """
    if not API_KEY:
        return {"error": "API key no configurada en .env"}

    try:
        parametros = {
            "key": API_KEY,
            "q": city_name,
            "lang": "es"
        }

        respuesta = requests.get(BASE_URL, params=parametros, timeout=10)
        respuesta.raise_for_status()

        data = respuesta.json()

        if "error" in data:
            return {"error": data["error"].get("message", "Error desconocido de la API.")}

        return data

    except requests.exceptions.Timeout:
        return {"error": "Tiempo de espera agotado."}

    except requests.exceptions.ConnectionError:
        return {"error": "Error de conexión."}

    except requests.exceptions.HTTPError as e:
        return {"error": f"Error HTTP: {e}"}

    except Exception as e:
        return {"error": f"Error inesperado: {e}"}