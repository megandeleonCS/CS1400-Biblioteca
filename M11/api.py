import requests

def obtener_coordenadas(nombre_ciudad):
    """
    Consulta la API Open-Meteo Geocoding para obtener 
    la latitud y longitud de una ciudad dada.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    parametros = {
        "name": nombre_ciudad,
        "count": 1,
        "language": "es",
        "format": "json"
    }
    
    try:
        # Hacemos la solicitud con un límite de tiempo de 10 segundos
        respuesta = requests.get(url, params=parametros, timeout=10)
        respuesta.raise_for_status()  # Lanza una excepción si hay un error HTTP (ej. 404 o 500)
        
        datos = respuesta.json()
        
        # Verificamos si la lista 'results' está vacía o no existe
        if "results" not in datos or not datos["results"]:
            print(f" No se encontró la ubicación: '{nombre_ciudad}'.")
            return None
        
        # Extraemos los datos del primer resultado obtenido
        lugar = datos["results"][0]
        info_lugar = {
            "nombre": lugar.get("name"),
            "pais": lugar.get("country", "Desconocido"),
            "lat": lugar.get("latitude"),
            "lon": lugar.get("longitude")
        }
        
        return info_lugar

    except requests.exceptions.RequestException as e:
        # Manejo de errores de red o conexión a internet
        print(f"Error de conexión: No se pudo contactar al servidor de la API.")
        return None