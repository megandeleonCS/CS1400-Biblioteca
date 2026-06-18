# ==========================================
# TAREA 1 - Introducción a Turtle 🐢
# ==========================================
# En esta actividad aprenderás a:
# 1. Mover la tortuga hacia adelante.
# 2. Girarla usando grados.
# 3. Dibujar un cuadrado.
# 4. Usar un bucle para repetir instrucciones.
#
# IMPORTANTE:
# - Un giro completo es de 360 grados.
# - Un cuadrado tiene 4 lados iguales.
# - Cada esquina de un cuadrado mide 90 grados.
#
# Completa todos los TODO.

# ------------------------------------------
# Importaciones necesarias
# ------------------------------------------
#from turtle import make_turtle, forward, left
import turtle


import turtle   # Importa el módulo turtle para dibujar

# 1. Iniciar ventana y objeto de tortuga
ventana = turtle.Screen()
t = turtle.Turtle() 
t.speed(3)


# ------------------------------------------
# Paso 1: Crear la ventana y la tortuga
# ------------------------------------------

# TODO:
# Crea la tortuga usando make_turtle().
# La ventana debe tener 400 de alto y 400 de ancho.

# Escribe aquí tu código
turtle.setup(width=400, height=400)

# ------------------------------------------
# Paso 2: Dibujar una línea
# ------------------------------------------

# TODO:
# Mueve la tortuga hacia adelante 100 pasos.
# Observa qué sucede.

# Escribe aquí tu código
turtle.forward(100)

# ------------------------------------------
# Paso 3: Girar la tortuga
# ------------------------------------------

# TODO:
# Gira la tortuga 90 grados hacia la izquierda.
# Luego avanza otros 100 pasos.

# Escribe aquí tu código
turtle.left(90)
turtle.forward(100)

# ------------------------------------------
# Paso 4: Dibujar un cuadrado (sin bucle)
# ------------------------------------------
# Un cuadrado tiene:
# - 4 lados
# - 4 giros de 90 grados

print("Dibujando un cuadrado sin bucle...")

# TODO:
# Completa los movimientos necesarios
# para dibujar un cuadrado de lado 100.
# Debes usar forward() y left() varias veces.
# La tortuga debe terminar donde empezó.

# Escribe aquí tu código
turtle.left(90)
turtle.forward(100) 
turtle.left(90)
turtle.forward(100)
turtle.left(90)

# ------------------------------------------
# Paso 5: Dibujar un cuadrado usando un bucle
# ------------------------------------------
# Ahora haremos lo mismo pero usando menos código.

print("Dibujando un cuadrado con bucle...")
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

# TODO:
# Usa un bucle for que repita 4 veces:
#   - avanzar 100
#   - girar 90 grados

# for ...:
#     forward(...)
#     left(...)


# ------------------------------------------
# Paso EXTRA (opcional)
# ------------------------------------------
# ¿Puedes dibujar un triángulo?
#
# Pista:
# - Un triángulo tiene 3 lados.
# - Un giro completo es 360 grados.
# - ¿Cuánto debe girar en cada esquina?

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

ventana.exitonclick()

