
"""# Manejo de textos y listas
mensaje = "bienvenido al curso de python"
comidas = ["tacos", "pizza", "hamburguesa"]
comidas.append("feijao tropeiro, galinhada, churrasco")
# Mostrar datos
print(mensaje.upper())
print(comidas[1])
#print(comidas)"""

"""playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Adam ha dejado el equipo. Use 'remove' para eliminarlo:
playerNames.remove("Adam")
# 2. Elimine el primer número de la lista (5) usando 'pop':
playerNumbers.pop(0)
# 3. Use 'append' para agregar estas variables a sus listas:
#name = "Lucas" 
#num = 7
playerNames.append("Lucas")
playerNumbers.append(7)
# 4. Use 'insert' para que "Raven" (número 1) sea la primera en la lista:
playerNames.insert(0,"Raven")
playerNumbers.insert(0, 1)
print(playerNames)
print(playerNumbers)""" 

"""import random

def Generate_Numbers():
    numbers = []
    for i in range(20):
        num = random.randint(1, 50)
        numbers.append(num)
    return numbers

# Llamada a la función
mis_numeros = Generate_Numbers()"""

"""def Even_Numbers(lista_origen):
    even = []
    # TODO: Itere la lista_origen y agregue a 'even' solo los números pares
    
    for num in lista_origen:
        if num % 2 == 0:
            even.append(num)
            
    return even

def Ten_Or_Less(lista_origen):
    # TODO: Cree una lista vacía, busque valores <= 10 y devuélvala
    numeros = []
    for num in lista_origen:
        if num <= 10: 
            numeros.append(num)
    return numeros

def Calcular_Diferencias(lista_origen):
    # TODO: Calcule la distancia entre números consecutivos
    # Ejemplo: [10, 7, 15] -> [3, 8]
    diferencias =[]
    for i in range(len(lista_origen) -1):
        a = lista_origen[i]
        b = lista_origen[i + 1]
        diferencia = abs(a - b)
        diferencias.append(diferencia )
    return diferencias"""


tictactoe = [
    ["X", "X", "X"],
    ["-", "O", "-"],
    ["O", "-", "-"]
]
if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
    print("Son iguales")
else:
    print("Diferentes")


# Escriba el 'if' para detectar si la fila superior (índice 0) tiene tres "X":
# Pista: Debe revisar las posiciones [0][0], [0][1] y [0][2]
