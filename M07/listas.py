# ==========================================
#  M7 Tarea Listas
#  Christian Mendoza  
#  Fecha: 2026-10-14
# ==========================================

# Manejo de textos y listas
mensaje = "bienvenido al curso de python"
comidas = ["tacos", "torta ahogada", "Mole"]

# Mostrar datos
print(mensaje.upper())
print(comidas[1])

"""
1. Ejecuta el código. ¿Cómo se muestra el texto de la variable mensaje en la consola?
-
bienvenido al curso de python

2. Observa la instrucción print(comidas[0]). ¿Qué comida se imprimió en pantalla y en qué posición de la lista se encuentra?
- tacos, en la posicion 0 de la lista.

*Modificación 1: Métodos de cadenas (Strings)

3. Ejecuta el programa modificado. ¿Qué cambio ocurrió en la salida del texto respecto al código original?
- La salida del texto de la variable "mensaje" se muestra toda en mayusculas.

*Modificación 2: Acceso a elementos de una lista
4. Cambia el índice dentro del corchete comidas[0] para mostrar en pantalla la segunda comida de tu lista. ¿Qué número de índice tuviste que utilizar y por qué?
- Tuve que poner el numero 1 por que en las listas se empieza a contar desde el 0.

5. Modifica la lista comidas para que incluya tres de tus alimentos favoritos reales y vuelve a imprimir únicamente la segunda opción.

Observa las opciones y complete las definiciones. Métodos disponibles: insert, append, remove, pop y clear.

6. ¿Qué método elimina todos los elementos de la lista? RESPUESTA: clear

7. ¿Qué método elimina un elemento de la lista por su valor de índice? RESPUESTA: pop

8. ¿Qué método elimina un elemento de la lista usando el valor del elemento? RESPUESTA: remove

9. ¿Qué método agrega un elemento al final de la lista? RESPUESTA: append

10. ¿Qué método agrega un elemento en una ubicación específica? RESPUESTA: insert

"""

#DESAFÍO DE CÓDIGO 1:
playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Adam ha dejado el equipo. Use 'remove' para eliminarlo:
playerNames.remove("Adam")

# 2. Elimine el primer número de la lista (5) usando 'pop':
playerNumbers.pop(0)

# 3. Use 'append' para agregar estas variables a sus listas:
name = "Lucas" 
num = 7
playerNames.append(name)
playerNumbers.append(num)

# 4. Use 'insert' para que "Raven" (número 1) sea la primera en la lista:
playerNames.insert(0, "Raven")
playerNumbers.insert(0, 1)

print("Nombres:", playerNames)
print("Números:", playerNumbers)
#Agregue estos ultimos print para verificar que esuvieran bien los cambios.

#Contadores e Iteradores (Counters and Iterators)
import random

def Generate_Numbers():
    numbers = []
    for i in range(20):
        num = random.randint(1, 50)
        numbers.append(num)
    return numbers

# Llamada a la función
mis_numeros = Generate_Numbers()

"""
11. ¿Qué tipo de datos se está agregando a la lista numbers? RESPUESTA: Se estan agregando numero enteros.

12. ¿Cuántos números se están agregando exactamente a la lista? RESPUESTA: se agregan 20 numeros por que en el "for" se puso un rango de 20.         

13. ¿Qué devuelve (return) la función al final de su ejecución? RESPUESTA: la lista "numbers" llena con los 20 numeros aleatorios.

"""

#DESAFÍO DE CÓDIGO 2:
def Even_Numbers(lista_origen):
    even = []
    # TODO: Itere la lista_origen y agregue a 'even' solo los números pares
    for num in lista_origen:
        if num % 2 == 0:  #Con % obtenemos el residuo de la division, entonces, si el residuo de dividirlo entre 2 es 0, significa que es par.
            even.append(num) #Va agregaando el numero al final de la lista
    return even

def Ten_Or_Less(lista_origen):
    # TODO: Cree una lista vacía, busque valores <= 10 y devuélvala
    menos_10 = []
    for num in lista_origen:
        if num <= 10:
            menos_10.append(num)
    return menos_10

    pass #No se si borrarlo, lo deje por si acaso, pero no hace nada.

def Calcular_Diferencias(lista_origen):
    # TODO: Calcule la distancia entre números consecutivos
    # Ejemplo: [10, 7, 15] -> [3, 8]
    diferencias = [] #Creamos la lista vacia donde se guardaran las diferencias despues del calculo.
    for i in range(len(lista_origen) - 1): #Con len contamos cuantos elementos hay y le agregamos -1 para que no se salga del rango de la lista.
        diferencia = abs(lista_origen[i] - lista_origen[i + 1])  #abs nos da el valor absoluto de la resta de los dos numeros.
        diferencias.append(diferencia)  #Lo vamos agregando a la lista.
    return diferencias

    pass #No se si borrarlo, lo deje por si acaso, pero no hace nada.

#Listas 2D (2D Lists)
#DESAFÍO DE CÓDIGO 3:
tictactoe = [
    ["X", "X", "X"],
    ["-", "O", "-"],
    ["O", "-", "-"]
]

# Escriba el 'if' para detectar si la fila superior (índice 0) tiene tres "X":
# Pista: Debe revisar las posiciones [0][0], [0][1] y [0][2]
if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
    print("Fila superior tiene tres X")
"""
¿Qué valor devolvería la instrucción tictactoe[1][1] en el tablero anterior? RESPUESTA: Devolveria 0 (el de en puro medio del tablero)

¿Para qué sirve un print() vacío que se coloca al final de un bucle que imprime una matriz? RESPUESTA: Hace un salto de linea para que se vea mas claro.

"""
