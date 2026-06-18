# utils.py

def limpiar_y_tokenizar(texto):
    """
    Limpia el texto convirtiéndolo a minúsculas y eliminando ruido básico.
    Devuelve una lista de palabras (tokens).
    """
    # Paso 1: Convertir a minúsculas con .lower()
    texto = texto.lower()
    
    # Paso 2: Reemplazos . con espacio y , con espacio usando .replace() (puedes añadir más si es necesario)
    texto = texto.replace('.', ' ').replace(',', ' ')

    
    # Paso 3: Dividir en palabras usando .split()
    palabras = texto.split()
    
    # Devuelve la lista de palabras
    return palabras