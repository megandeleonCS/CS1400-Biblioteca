""" TODO 1 agregar tu nombre fecha titulo de una manera bonita """
# ==========================================
# M6 Proyecto Tortuga 
#  Christian Mendoza  
#  Fecha: 2026-10-06
# ==========================================

# Importamos la biblioteca turtle (ya viene incluida en Python)
import turtle

# Configuración de la pantalla y la tortuga
pantalla = turtle.Screen() # # Usamos sintaxis de punto . para acceder a la función Screen()
pantalla.bgcolor("White")  # TODO 2 Cambia el color de fondo usando la función bgcolor()
pantalla.title("Proyecto Tortuga") #TODO 3 Asigna un título a la ventana usando title()

# Corre el programa hasta este punto utilizando """ """ o # para asegurar que funcione bien.

# solo una t para hacer menos codigo despues. usaremos la t variable para usar otras funciones.
t = turtle.Turtle()
t.shape("turtle")  # Forma de la tortuga puede ser cualquier otro nombre.
t.speed(3)         # Velocidad del dibujo (1 es lento, 10 es rápido)

# TODO 4  para correr el programa hasta este punto y toma una captura de pantalla. Luego lo guardaras entre la carpeta M6
# TODO 4 para correr el programa hasta este punto y toma una captura de pantalla. Luego lo guardaras entre la carpeta M6

# =============================================================
# EJEMPLO: Dibujar la base de la casa (un cuadrado azul)
# =============================================================

t.color("red", "darkblue")  # (Color del borde, Color de relleno - los puedes ajustar si deseas - TODO 5 los colores son parametros o argumentos?) 
# SON ARGUMENTOS por que se les esta dando el valor real que se envía a la función cuando se la llama.
t.begin_fill()

# TODO 6 Este for loop que hace? Repite 4 veces las instrucciones de avanzar 100 para delante y girar 90° a la izquierda.
for _ in range(4):
    t.forward(100)  # 
    t.left(90)      # 

# TODO 7 En que linea de codigo empezo el fill? o relleno? en la linea 31 con t.begin_fill().
t.end_fill()

# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()
