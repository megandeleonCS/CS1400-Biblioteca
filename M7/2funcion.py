# --------------------------------------------------------------------------
#          FUNCIÓN PARA CALCULAR EL ÁREA DE UN RECTÁNGULO
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que reciba el largo y el ancho de un
# rectángulo y devuelva su área.
#
# Instrucciones para el estudiante:
# 1. Completa la función `calcular_area_rectangulo`.
# 2. La función esta recibiendo dos argumentos: `largo` y `ancho`.
# 3. Dentro de la función, calcula el área (largo * ancho).
# 4. La función debe devolver el área calculada usando una nueva variable 'area' y la sentencia `return`.
# --------------------------------------------------------------------------

def calcular_area_rectangulo(largo, ancho):
    
    """
    Calcula el área de un rectángulo.

    Args:
      largo (float or int): El largo del rectángulo.
      ancho (float or int): El ancho del rectángulo.

    Returns:
      float or int: El área calculada del rectángulo.
    """
    # TODO: Paso 1. Calcula el área. La fórmula es largo * ancho.
    
    area = largo * ancho

    # TODO: Paso 2. Devuelve el valor calculado.
    # Reemplaza 'None' con la variable que contiene el área.
    return area


# --- Bloque para probar tu función ---
# Este código no será calificado, es solo para que pruebes tu función.
# Puedes modificar los valores de `largo_prueba` y `ancho_prueba`.
if __name__ == "__main__":
    # Ejemplo 1
    largo_prueba = 10
    ancho_prueba = 5

    # Llamada a la función
    area_resultado = calcular_area_rectangulo(largo_prueba, ancho_prueba)

    # Imprimir el resultado
    print(
        f"El área de un rectángulo con largo {largo_prueba} y ancho {ancho_prueba} es: {area_resultado}")

    # Ejemplo 2
    largo_prueba_2 = 7.5
    ancho_prueba_2 = 3
    area_resultado_2 = calcular_area_rectangulo(largo_prueba_2, ancho_prueba_2)
    print(
        f"El área de un rectángulo con largo {largo_prueba_2} y ancho {ancho_prueba_2} es: {area_resultado_2}")