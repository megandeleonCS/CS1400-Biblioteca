"""Tarea 1: Preparando la Oferta (Listas y Tuplas)

"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]
ofrendas.append("Incienso copal")
ofrendas.sort()
print(ofrendas)
print("Segunda ofrenda:", ofrendas[1])

for i in enumerate(ofrendas):
    enumerate(i)
"""
# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)

NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")
NIVELES_ALTAR[0] = "Gloria"
# Mostrar la segunda ofrenda (índice 1)



Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
#1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
 .append("Incienso copal") y luego ordena la lista alfabéticamente usando
 la función .sort().  ¿Qué notas del variable en linea #12?
#Utilizando .sort(), la lista se ordenó alfabéticamente.

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
 NIVELES_ALTAR[0] = "Gloria".
 ¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?
#Genera un TypeError porque es una tupla y no se puede modificar una vez creada.

#3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
 de tu lista junto con su número de posición en el altar."""

 


