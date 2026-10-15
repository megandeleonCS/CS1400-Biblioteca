# ==========================================
# TAREA Turtle 🐢
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

import turtle
# La siguiente linea agrega funciones para realizar la tarea en nuestro programa
#from turtle import make_turtle, forward, left
def make_turtle():
    nueva_tortuga = turtle.Turtle()
    nueva_tortuga.shape("turtle")
    return nueva_tortuga
# ------------------------------------------
# Crear la ventana y la tortuga
# ------------------------------------------

# TODO 1
#  Iniciar ventana y objeto de tortuga y agregar el speed o velocidad. Pista: Mira la Tarea 1turtle.py

# Escribe aquí tu código
pantalla = turtle.Screen()
pantalla.bgcolor("White")
pantalla.title("Tortuguita Casa") 

# TODO 2
#  Crea la tortuga usando make_turtle(). 
"""
Esta parte no la entendi, no me importaba make_turtle() y mejor la defini yo.
"""
#  La ventana debe tener 400 de alto y 400 de ancho.

# Escribe aquí tu código
pantalla.setup(width=400, height=400)
t = make_turtle()
t.speed(3)  


# Captura de Pantalla, nombralo "TUNOMBRE_1_2" y guardalo en la carpeta M06

# ------------------------------------------
# Dibujar una línea
# ------------------------------------------

# TODO 3:
# Mueve la tortuga hacia adelante 100 pasos.
# Observa qué sucede.

# Escribe aquí tu código
t.forward(100)

# ------------------------------------------
# Girar la tortuga
# ------------------------------------------

# TODO 4:
# Gira la tortuga 90 grados hacia la izquierda.
# Luego avanza otros 100 pasos.

# Escribe aquí tu código
t.left(90)
t.forward(100)


# ------------------------------------------
# Dibujar un cuadrado 
# ------------------------------------------
# Un cuadrado tiene:
# - 4 lados
# - 4 giros de 90 grados

print("Dibujando un cuadrado...")

# TODO 5:
# Completa los movimientos necesarios
# para dibujar un cuadrado de lado 100.
# Debes usar forward() y left() varias veces.
# La tortuga debe terminar donde empezó.

# Escribe aquí tu código
t.left(90) #La tortuga gira 90 grados a la izquierda
t.forward(100) #La tortuga avanza 100 pasos hacia adelante
t.left(90) #La tortuga gira 90 grados a la izquierda
t.forward(100) #La tortuga avanza 100 pasos hacia adelante
t.left(90)  #La tortuga gira 90 grados a la izquierda para acabar donde comenzo

# ------------------------------------------
# Paso EXTRA (opcional)
# ------------------------------------------
# ¿Puedes agregar un triángulo? y un rectangulo? Dibuja una casita.
#
# Pista:
# - Un triángulo tiene 3 lados.
# - Un giro completo es 360 grados.
# - ¿Cuánto debe girar en cada esquina?

t.forward(100) # Movemos la tortuga a la esquina inferior derecha
t.left(90)     # Damos media vuelta
t.forward(100)  # Avanzamos hasta la esquina superior izquierda
t.left(30) #Se gira la tortuga 30 grados para la izquierda
t.forward(100)  # Avanzamos para arriba 
t.left(120) # Se gira la tortuga a la izquiera para ir de regreso
t.forward(100)  # La tortuga baja para completar el techo


# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()