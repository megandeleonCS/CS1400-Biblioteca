"""
====================================================================
Proyecto: Dibujar una pizza con Python Turtle
====================================================================
En este ejercicio aprenderás el PODER DE LAS FUNCIONES:
1. Reutilización: Escribe el código una vez y úsalo muchas veces.
2. Modularidad: Rompe un problema grande (una tarta) en problemas 
   pequeños (porciones/triángulos).
3. Parámetros: Cambia el comportamiento de tu dibujo pasando 
   diferentes argumentos (tamaño, número de rebanadas, color).
====================================================================
"""

import math
import turtle

# ==================================================================
# 1. Configuración Inicial del Entorno
# ==================================================================
pantalla = turtle.Screen()
pantalla.bgcolor("lightcyan")
pantalla.title("El Poder de las Funciones: Tarta de Triángulos")

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)


# ==================================================================
# 2. Definición de Funciones
# ==================================================================

# TODO 1: Completa la definición de la función 'dibujar_triangulo'
def dibujar_triangulo(t, longitud=100, angulo=60, color_relleno="orange"):
    """
    Dibuja una porción de tarta (triángulo isósceles) usando la tortuga 't'.
    
    Parámetros:
    - t: El objeto Turtle que dibuja.
    - longitud: La longitud de los dos lados iguales (el radio de la tarta).
    - angulo: El ángulo en el vértice central (en grados).
    - color_relleno: El color con el que se pintará la porción.
    """
    
    # --------------------------------------------------------------
    # Paso A: Cálculos Matemáticos (Geometría del Triángulo)
    # --------------------------------------------------------------
    
    # 1. Convertimos la mitad del ángulo a radianes para usar trigonometría
    angulo_radianes = math.radians(angulo / 2)
    # TODO 2: Calcula la longitud de la base del triángulo isósceles.
    # FÓRMULA: 

    base = 2 * longitud * math.sin(angulo_radianes)
    
    # TODO 3: Calcula el ángulo de giro exterior para la tortuga en las esquinas.
    # Pista: La suma de ángulos internos de un triángulo es 180°.
    # El ángulo en la base es: (180 - angulo) / 2.
    # El giro exterior es: 180 - ángulo_base  =>  90 + (angulo / 2)

    angulo_giro_base = 180 - (180 - angulo) / 2
    

    # --------------------------------------------------------------
    # Paso B: Dibujo del Triángulo Isósceles
    # --------------------------------------------------------------
    t.color("darkred", color_relleno)
    t.begin_fill()
    
    # TODO 4: Escribe el trazado del triángulo con 'forward' y 'left'.
    # 1. Avanza 'longitud' (Lado 1)
    # 2. Gira 'angulo_giro_base' hacia la izquierda
    # 3. Avanza 'base' (La corteza de la tarta)
    # 4. Gira 'angulo_giro_base' hacia la izquierda
    # 5. Avanza 'longitud' (Lado 2 para regresar al centro)
    # 6. Gira 180° para quedar orientado en dirección opuesta
    

    # tu codigo faltante aqui
    t.forward(longitud)               # 1. Avanza 'longitud' (Lado 1)
    t.left(angulo_giro_base)      # 2. Gira 'angulo_giro_base' hacia la izquierda
    t.forward(base)                   # 3. Avanza 'base' (La corteza de la tarta)
    t.left(angulo_giro_base)      # 4. Gira 'angulo_giro_base' hacia la izquierda
    t.forward(longitud)               # 5. Avanza 'longitud' (Lado 2 para regresar al centro)
    t.left(180)                       # 6. Gira 180° para quedar orientado en dirección opuesta
    
    t.end_fill()


# TODO 5: Función que reutiliza 'dibujar_triangulo' para construir la tarta completa. 
# Parametros incluyen porciones, longitud, y el color del relleno.

    """
    Dibuja una tarta completa de 'n_porciones' llamando repetidamente
    a la función 'dibujar_triangulo'.
    """
def dibujar_tarta(t, n_porciones, longitud, color_relleno):
    
    # TODO 6: Calcula el ángulo central de cada porción (360° / n_porciones)
    angulo = 360 / n_porciones

    
    # TODO 7: Usa un bucle 'for' para dibujar todas las porciones llamando la funcion dibujar_triangulo
    for _ in range(n_porciones):
        dibujar_triangulo(t, longitud, angulo, color_relleno)

# TODO 8 (EXTRA/OPCIONAL): Función auxiliar para mover la tortuga sin dejar rastro
def mover_tortuga(t, x, y):
    """Mueve la tortuga a las coordenadas (x, y) sin dibujar."""
    # Investigar .penup .goto y .pendown
    t.penup() #"Levantar pluma". Todo lo que camine la tortuga a partir de este instante no pintará ninguna línea.
    t.goto(x, y) #"Ir a la coordenada (x, y)". Mueve a la tortuga directamente al punto del plano cartesiano especificado.
    t.pendown() #"Bajar pluma". Todo lo que camine la tortuga a partir de este instante sí pintará líneas.


# ==================================================================
# 3. Demostración del Poder de las Funciones
# ==================================================================
# ¡Mira qué fácil es dibujar varias tartas completas en diferentes 
# posiciones, con distintos números de porciones, tamaños y colores!
# TODO 9: aqui deben ir tus instrucciones para dibujar.

# --- Tarta 1: Tarta clásica de 6 porciones ---
mover_tortuga(t, -200, 0)
dibujar_tarta(t, n_porciones=6, longitud=80, color_relleno="orange")

# --- Tarta 2: Tarta grande de 12 porciones ---
mover_tortuga(t, 0, 0)
dibujar_tarta(t, n_porciones=12, longitud=100, color_relleno="blue")

# --- Tarta 3: Tarta pequeña (o pizza) de 4 porciones ---
mover_tortuga(t, 200, 0)
dibujar_tarta(t, n_porciones=4, longitud=60, color_relleno="green")

# TODO 10: Finalizar ejecución al hacer clic
pantalla.exitonclick()