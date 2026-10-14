""" TODO 1 agregar tu nombre fecha titulo de una manera bonita """
# Marcos Alves oct. 6, 2026

# Importamos la biblioteca turtle (ya viene incluida en Python)
import turtle

# Configuración de la pantalla y la tortuga
pantalla = turtle.Screen() # # Usamos sintaxis de punto . para acceder a la función Screen()
pantalla.bgcolor("lightgreen")  # TODO 2 Cambia el color de fondo usando la función bgcolor()
pantalla.title("felicidade") #TODO 3 Asigna un título a la ventana usando title()

# Corre el programa hasta este punto utilizando """ """ o # para asegurar que funcione bien.

# solo una t para hacer menos codigo despues. usaremos la t variable para usar otras funciones.
t = turtle.Turtle()
t.shape("turtle")  # Forma de la tortuga puede ser cualquier otro nombre.
t.speed(3)         # Velocidad del dibujo (1 es lento, 10 es rápido)

# TODO 4 para correr el programa hasta este punto y toma una captura de pantalla. Luego lo guardaras entre la carpeta M6

# =============================================================
# EJEMPLO: Dibujar la base de la casa (un cuadrado azul)
# =============================================================

t.color("darkblue", "lightblue")  # (Color del borde, Color de relleno - los puedes ajustar si deseas - TODO 5 los colores son parametros o argumentos?)
t.begin_fill()

# TODO 6 Este for loop que hace que? diz como a tarataruga deve andar.
for _ in range(4):
    t.forward(100)  # 
    t.left(90)      # 

# TODO 7 En que linea empezo el fill? o relleno? na linha 26 
t.end_fill()

# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()
