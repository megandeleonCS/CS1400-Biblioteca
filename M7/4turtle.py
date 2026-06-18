# ================================
# Proyecto: Dibujar una tarta con Turtle
# ================================
# En este ejercicio vas a:
# 1. Usar trigonometría para calcular la base de un triángulo isósceles.
# 2. Dibujar un triángulo con turtle.
# 3. Repetir el triángulo varias veces para formar una "tarta".

# ¡Lee cada paso con atención y completa los TODO!

# Importaciones necesarias

# from turtle import make_turtle, forward, left, right, penup, pendown
import math
from turtle import make_turtle, forward, left, right, penup, pendown

def triangulo(t, longitud, angulo):
    angulo_rad = math.radians(angulo)

    """
    TODO Paso 1:
    Escribe aquí qué hace esta función.
#Dibuja un triángulo isósceles que representa una porción de la tarta

    Pista:
    - ¿Qué representa 'longitud'? es el largo de los dos lados iguales, los radios desde el centro.
    - ¿Qué representa 'angulo'? es el area central entre esos 2 radios medida e grados)
    - ¿Qué debería dibujar esta función? Dibuja un triángulo isósceles que representa una porción de la tarta
    """
    
    # --------------------------------
    # Paso 2: Cálculos matemáticos
    # --------------------------------
    
    # Convierte el ángulo a radianes para poder usar funciones trigonométricas.
    angulo_rad = math.radians(angulo)
    
    # TODO:
    # Calcula la longitud de la base del triángulo isósceles.
    # Pista: estás trabajando con dos lados iguales (longitud)
    # y el ángulo central entre ellos.
    # Puedes usar math.sin().
    # Base del triangulo (cuerda del circulo):
    # base = 2 * L * sin(angulo / 2)

    base =  2 * longitud * math.sin(angulo_rad / 2)

    # Angulos de la base (internos): (180 - angulo) / 2
    
    angulo_base = (180 - angulo) / 2
    
    # TODO:
    # Calcula el ángulo que debe girar la tortuga en las esquinas
    # para que el triángulo se cierre correctamente.
    # = 90 + angulo/2
    
    angulo_giro = 180 - angulo_base


    # --------------------------------
    # Paso 3: Dibujo del triángulo
    # --------------------------------
    
    # Dibuja el triángulo usando forward() y left().
    # Recuerda:
    # - Debes dibujar dos lados iguales (longitud).
    # - Debes dibujar la base.
    # - La tortuga debe volver al punto inicial.
    
    # TODO:
    # Escribe aquí los movimientos necesarios.
    # Desde el centro: primer lado (radio)
    # Girar para dibujar la base
    # Girar para regresar al centro
    # Cerrar el triangulo para que el bucle funcione

    t = turtle.Turtle()
    
    t.forward(longitud)

    t.left(angulo_giro)
    t.forward(base)
   
    t.left(angulo_giro)
    t.forward(longitud)

    t.right(180 + angulo)

def dibujar_tarta(n_porciones, longitud):
    """
    TODO:
    Explica qué hace esta función.
    #Dibuja una tarta o círculo formada por 'n_porciones' triángulos isósceles.
    
    Pista:
    - ¿Qué es n_porciones? Las porciones que tendra una tarta
    - ¿Qué representa longitud? el tamano de la tarta o el largo de cada radio
    """
    
    # --------------------------------
    # Paso 4: Calcular el ángulo de cada porción
    # --------------------------------
    
    # TODO:
    # Calcula el ángulo central de cada porción.
    # Pista: un círculo completo tiene 360 grados.

    angulo_porcion =  360 / n_porciones
    
    # --------------------------------
    # Paso 5: Dibujar todas las porciones
    # --------------------------------
    
    # TODO:
    # Escribe un bucle for que:
    # 1. Llame a la función triangulo(...)
    # 2. Gire la tortuga el ángulo necesario
    #    para dibujar la siguiente porción.
    
    ###### for _ in range(n_porciones):
        # triangulo(...)
        # turtle.left(...)
        pass
########

    # for ...:
    #     triangulo(...)
    #     left(...)

    def triangulo(t, longitud, angulo):

     for _ in range(n_porciones):
        triangulo(t, longitud, angulo_porcion)
        t.left(angulo_porcion)

# ==================================
# Bloque para probar la función
# ==================================
####turtle.speed(5) # Ajusta la velocidad (1-10)
#####turtle.shape("turtle")

make_turtle(height=400, width=600)

# ----------------------------------
# Prueba 1
# ----------------------------------

print("Dibujando una tarta de 5 porciones...")
dibujar_tarta(5, 80)

# ----------------------------------
# TODO EXTRA
# ----------------------------------
# 1. Levanta el lápiz (penup()).
t.pendown()

# 2. Muévete a otra posición.

t.right(90)
t.forward(150)
t.left(90)

# 3. Baja el lápiz (pendown()).

t.pendown()

# 4. Dibuja otra tarta con diferentes valores.
#### turtle.penup()
#### turtle.goto()

# ----------------------------------
# Prueba 2
# ----------------------------------

print("Dibujando una tarta de 8 porciones...")
dibujar_tarta(8, 60)
####turtle.done()