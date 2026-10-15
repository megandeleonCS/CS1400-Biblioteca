"""
NOMBRE: [CHRISTIAN MENDOZA]
FECHA: 22 SEPTIEMBRE 2026
MODULO 4 - TAREA 2
CANCION FAVORITA
Uso de manipulación de cadenas, operadores de comparación y sentencias if/else.
"""

# Python es poderoso y contiene varios métodos para manipular cadenas. 
# Uno de ellos es .rjust(ancho), que alinea el texto a la derecha.

# TODO Tarea 1: Pedir al usuario que escriba su línea favorita de una canción
linea = input("Escribe una línea de tu canción favorita: ")

# TODO Tarea 2: Crear una variable booleana para verificar que la línea no esté vacía
# Usa un operador de comparación (por ejemplo, verificar si el largo de la cadena es mayor a 0)
es_valida = len(linea.strip()) > 0  # Reemplaza con tu código (ej: len(linea) > 0)
# Verifica si la línea ingresada no está vacía y almacena el resultado en 'es_valida'. y el .strip() elimina espacios en blanco.


# TODO Tarea 3: Usa una estructura if/else 
# Si 'es_valida' es True, alinea el texto a la derecha con .rjust(80) e imprímelo.
# De lo contrario, imprime un mensaje de error pidiendo que escriban algo.
if not es_valida:
    print("Error: No ingresaste ninguna línea.")#imprime un mensaje de error si la línea está vacía
elif len(linea) > 50:
    print("La línea es demasiado larga.") #imprime un mensaje si la línea tiene más de 50 caracteres
else:
    linea_alineada = linea.rjust(80) #Si es true, alinea la línea a la derecha.
    print(linea_alineada) #imprime la línea alineada a la derecha

# TODO Reto: Agrega una condición adicional para verificar si la línea tiene más de 50 caracteres 
# y muestra un mensaje diferente si es demasiado larga.