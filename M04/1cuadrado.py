"""
#MODIFIQUE ESTO PARA CUMPLIR CON EL LABORATORIO PRECENSIAL 1 DE 2
NOMBRE: CHRISTIAN MENDOZA 
FECHA: 22 SEPTIEMBRE 2026
MODULO 4 - PROYECTO - TAREA 1
Un programa para encontrar el cuadrado de un número y evaluar condiciones.
"""

# Definir el número base - Hard Coded
#num = 4
num = int(input("Ingresa un numero para sacar su cuadrado y evaluar si es positivo o negativo: "))

# TODO Tarea 1: Crear una variable para almacenar el cuadrado (debe ser el numero base multiplicado por sí mismo)
cuadrado = num * num  # Reemplaza con tu código
# AL MULTIPLICAR UN NUMERO POR SI MISMO, SE SACA EL CUADRADO.

# Mostrar el resultado con un f-string 
print(f"El cuadrado de {num} es: {cuadrado}")

# Salida esperada:
# El cuadrado de 4 es: 16

# TODO Tarea 2: Usa un operador de comparación para verificar si el número es positivo (mayor que 0).
# Guarda el valor booleano (True o False) en una variable llamada 'es_positivo'.
es_positivo = num > 0  # Reemplaza con tu código
# Verifica si el número es positivo y almacena el resultado en 'es_positivo'.

# TODO Tarea 3: Agrega una estructura if/else 
# Si el número es positivo, imprime un mensaje diciendo que lo es. De lo contrario, imprime otro mensaje.
if es_positivo:
    print("El número es positivo.")
else:
    print("El número es negativo.")

"""
# TODO Reto: Modifica la variable 'num' para que sea ingresado por el usuario usando la función input().
# Recuerda convertir el valor ingresado a entero usando int().

"""