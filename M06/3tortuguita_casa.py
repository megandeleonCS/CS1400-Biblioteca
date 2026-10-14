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


# La siguiente linea agrega funciones para realizar la tarea en nuestro programa
#from turtle import make_turtle, forward, left


# ------------------------------------------
# Crear la ventana y la tortuga
# ------------------------------------------

# TODO 1
#  Iniciar ventana y objeto de tortuga y agregar el speed o velocidad. Pista: Mira la Tarea 1turtle.py

# TODO 2
#  Crea la tortuga usando make_turtle().
#  La ventana debe tener 400 de alto y 400 de ancho.
import turtle
# Escribe aquí tu código
pantalla = turtle.Screen()
pantalla.setup(400,400)

 
t = turtle.Turtle()
t.shape("turtle")  # Forma de la tortuga puede ser cualquier otro nombre.
t.speed(3)         # Velocidad del dibujo (1 es lento, 10 es rápido)

 
  
# Captura de Pantalla, nombralo "TUNOMBRE_1_2" y guardalo en la carpeta M06

# ------------------------------------------
# Dibujar una línea
# ------------------------------------------

# TODO 3:
# Mueve la tortuga hacia adelante 100 pasos.
# Observa qué sucede.
#
# Escribe aquí tu código
#t.forward(100)

# ------------------------------------------
# Girar la tortuga
# ------------------------------------------

# TODO 4:
# Gira la tortuga 90 grados hacia la izquierda.
# Luego avanza otros 100 pasos.

# Escribe aquí tu código
#t.left(90)
#t.forward(100)
# ------------------------------------------
# Dibujar un cuadrado 
# ------------------------------------------
# Un cuadrado tiene:
# - 4 lados
# - 4 giros de 90 grados

#print("Dibujando un cuadrado...")

# TODO 5:
# Completa los movimientos necesarios
# para dibujar un cuadrado de lado 100.
# Debes usar forward() y left() varias veces.
# La tortuga debe terminar donde empezó.

# Escribe aquí tu código
t.penup()
t.goto(0,0)
t.pendown()

for i in range(4):
    t.forward(100)
    t. left(90)

t.penup()
t.goto(100,0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)
# ------------------------------------------
# Paso EXTRA (opcional)
# ------------------------------------------
# ¿Puedes agregar un triángulo? y un rectangulo? Dibuja una casita.
#
# Pista:
# - Un triángulo tiene 3 lados.
# - Un giro completo es 360 grados.
# - ¿Cuánto debe girar en cada esquina? 3 veses
t.penup()
t.goto(0,100)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.forward(200)
t.pendown()
t.left(90)
t.forward(86.60)
t.left(90)
t.forward(150)
t.penup()
t.goto(-20,0)
# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()