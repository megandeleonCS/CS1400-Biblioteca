#### Ejemplo 1

num = int(input("Introduce un número entre 10 y 20: "))
print("Contando hacia arriba")
for i in range(0, num, 1):
    print(i)
print("Contando hacia abajo")
for i in range(num, 0, -1):
    print(i)

    #### Ejemplo 2
"""
    num = int(input("Introduce un número positivo o negativo (0 para salir): "))

negativos = 0

positivos = 0

while num != 0:

    if num < 0:

        print("El número es negativo")

        negativos += 1

    else:

        print("El número es positivo")

        positivos += 1

    num = int(input("Introduce un número positivo o negativo (0 para salir): "))

print("Total negativos:", negativos)

print("Total positivos:", positivos)
"""

num = int(input("Introduce un número entre 10 y 20: "))

print("Contando hacia arriba")
for i in range(0, num, 1):
    print(i)

print("Contando hacia abajo")
for i in range(num, 0, -1):
    print(i)

# range(0, num, 1): Genera una secuencia desde 0 hasta num - 1 incrementando de 1 en 1.

# range(num, 0, -1): Genera una secuencia descendente desde num hasta 1 decrementando de 1 en 1.

num = int(input("Introduce un número positivo o negativo (0 para salir): "))

negativos = 0
positivos = 0

while num != 0:
    if num < 0:
        print("El número es negativo")
        negativos += 1
    else:
        print("El número es positivo")
        positivos += 1
    
    num = int(input("Introduce un número positivo o negativo (0 para salir): "))

print("Total negativos:", negativos)
print("Total positivos:", positivos)

# Utiliza un bucle while que se mantiene activo mientras el número introducido sea diferente de 0.

# Si el número es menor a cero, incrementa la variable negativos. Si es mayor, incrementa positivos.

# Al finalizar el bucle (cuando se introduce 0), muestra los totales acumulados.