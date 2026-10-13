"""
NOMBRE: grecia lopez orozoco 
MODULO 4 - TAREA 2
CANCION FAVORITA
Uso de manipulación de cadenas, operadores de comparación y sentencias if/else.
"""

# Python es poderoso y contiene varios métodos para manipular cadenas. 
# Uno de ellos es .rjust(ancho), que alinea el texto a la derecha.

# TODO Tarea 1: Pedir al usuario que escriba su línea favorita de una canción
# Le pido al usuario que escriba una frase de una cancion
linea = input("Escribe una línea de tu canción favorita: ")

# TODO Tarea 2: Crear una variable booleana para verificar que la línea no esté vacía
# Usa un operador de comparación (por ejemplo, verificar si el largo de la cadena es mayor a 0)
# Reviso el tamano del texto para confirmar que no este vacio
es_valida = len(linea) > 0


# TODO Tarea 3: Usa una estructura if/else 
# Si 'es_valida' es True, alinea el texto a la derecha con .rjust(80) e imprímelo.
# De lo contrario, imprime un mensaje de error pidiendo que escriban algo.

# TODO Reto: Agrega una condición adicional para verificar si la línea tiene más de 50 caracteres 
# y muestra un mensaje diferente si es demasiado larga.

# Primero valido que si se haya escrito algo en la linea
if es_valida:
    # Si la frase mide mas de 50 caracteres, muestro un mensaje diferente
    if len(linea) > 50:
        print("Atención: La línea es demasiado larga (tiene más de 50 caracteres).")
    else:
        # Si mide 50 o menos, la alineo a la derecha usando 80 espacios
        linea_alineada = linea.rjust(80)
        print(linea_alineada)
else:
    # Si la persona no escribio nada, mando mensaje de error
    print("Error: No ingresaste ninguna línea.")