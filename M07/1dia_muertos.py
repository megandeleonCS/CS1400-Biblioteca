# ==========================================
#  M7 Proyecto Dia De Los Muertos
#  Christian Mendoza  
#  Fecha: 2026-10-14
# ==========================================

"""Tarea 1: Preparando la Oferta (Listas y Tuplas)

"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]
ofrendas.append("Incienso copal")
ofrendas.sort()
print(ofrendas) #Para corroborar que se agfego el incienso.

# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)

NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")
#NIVELES_ALTAR[0] = "Gloria"

# Mostrar la segunda ofrenda (índice 1)
print("\nSegunda ofrenda:", ofrendas[1]) #LE AGREGUE EL SALTO DE LINEA NOMAS PARA QUE SE VEA MEJOR

"""
Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
#1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
 .append("Incienso copal") y luego ordena la lista alfabéticamente usando
 la función .sort().  ¿Qué notas del variable en linea #12?

 -Si se refiere a "NIVELES_ALTAR", no modifica nada, ya que lo que se modifico fue la lista "ofrendas".

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
 NIVELES_ALTAR[0] = "Gloria".
 ¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?

 -Me da el error: TypeError: 'tuple' object does not support item assignment, y da ese error por que las tuplas no se pueden modificar una vez creadas.

#3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
 de tu lista junto con su número de posición en el altar.
"""
print("Ofrendas del altar:") #NOMAS SE LO AGREGUE PARA QUE SE VEA MAS BONITO.
for posicion, ofrenda in enumerate(ofrendas):
    print(f"{posicion}: {ofrenda}")

#LA SIGUIENTE PARTE LA HICE SOLO POR PRACTICA Y POR QUE ME ENCANTA EL DIA DE MUERTOS XD
print() #QUISE UTILIZAR UN PRINT VACIO EN VEZ DE UN SALTO DE LINEA NOMAS PARA VER SI FUNCIONABA IGUAL 
print("Niveles del altar:")
for posicion, nivel in enumerate(NIVELES_ALTAR):
    print(f"{posicion}: {nivel}")

