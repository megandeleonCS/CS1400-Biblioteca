# ================================
# Proyecto: Dibujar una tarta con Turtle
# ================================
# En este ejercicio vas a:
# 1. Usar trigonometría para calcular la base de un triángulo isósceles.
# 2. Dibujar un triángulo con turtle.
# 3. Repetir el triángulo varias veces para formar una "tarta".
#
# ¡Lee cada paso con atención y completa los TODO!

# Importaciones necesarias
import math

import turtle
turtle.speed(0)  # Aumenta la velocidad de dibujo   

#from turtle import make_turtle, forward, left, right, penup, pendown
import turtle

# 1. Iniciar ventana y objeto de tortuga
window = turtle.Screen()
t = turtle.Turtle() 
t.speed(3)



def triangulo(longitud, angulo):
    """
    TODO Paso 1:
    Escribe aquí qué hace esta función.
    
    Pista:
    - ¿Qué representa 'longitud'?
    - ¿Qué representa 'angulo'?
    - ¿Qué debería dibujar esta función?
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

    base = 2 * longitud * math.sin(angulo_rad / 2) 
    
    # TODO:
    # Calcula el ángulo que debe girar la tortuga en las esquinas
    # para que el triángulo se cierre correctamente.

    angulo_esquina = (180 - angulo) / 2  

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

    turtle.forward(longitud)
    turtle.left(180 - angulo_esquina)   
    turtle.forward(base)
    turtle.left(180 - angulo_esquina)  
    turtle.forward(longitud)
    turtle.left(180)  
    
    

def dibujar_tarta(n_porciones, longitud):
    """
    TODO:
    Explica qué hace esta función.
    
    Pista:
    - ¿Qué es n_porciones?
    - ¿Qué representa longitud?
    """
    
    # --------------------------------
    # Paso 4: Calcular el ángulo de cada porción
    # --------------------------------
    
    # TODO:
    # Calcula el ángulo central de cada porción.
    # Pista: un círculo completo tiene 360 grados.

    angulo_porcion = 360 / n_porciones 
    
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
    
    for i in range(n_porciones):
        triangulo(longitud, 360 / n_porciones)
        turtle.left(360 / n_porciones)
        


# ==================================
# Bloque para probar la función
# ==================================
####turtle.speed(5) # Ajusta la velocidad (1-10)
#####turtle.shape("turtle")


ventana = turtle.Screen()
ventana.setup(width=600, height=400)

#make_turtle(height=400, width=600)


# ----------------------------------
# Prueba 1
# ----------------------------------

print("Dibujando una tarta de 5 porciones...")
turtle.penup()
turtle.goto(100, 0)  # Mueve la tortuga a una nueva posición
turtle.pendown()
print("Dibujando una tarta de 5 porciones...")
dibujar_tarta(5, 80)
# ----------------------------------
# TODO EXTRA
# ----------------------------------
# 1. Levanta el lápiz (penup()).
# 2. Muévete a otra posición.
# 3. Baja el lápiz (pendown()).
# 4. Dibuja otra tarta con diferentes valores.
#### turtle.penup()
#### turtle.goto()


# ----------------------------------
# Prueba 2
# ----------------------------------

print("Dibujando una tarta de 8 porciones...")

turtle.penup()
turtle.goto(-150, 0)  # Mueve la tortuga a una nueva posición
turtle.pendown()
print ("Dibujando una tarta de 8 porciones...")
dibujar_tarta(8, 80)

turtle.done()  # Mantiene la ventana abierta hasta que el usuario la cierre

dibujar_tarta(8, 60)
####turtle.done()

