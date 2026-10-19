## 📗 Calcular el Área de Varios Círculos (Práctica de Iteraciones)
"""'''
### Instrucciones:
1. Descomenta la linea que dejara importar el módulo math.
2. Crea una lista con los radios: [5, 12, -3, 8, 0].
3. Utiliza un bucle for para recorrer cada radio de la lista.
4. Dentro del bucle, usa un condicional if/else para calcular y mostrar el área únicamente si el radio es mayor que 0.
5. Reto de Iteración Continuada: Cambia la estructura a un bucle while que le pida al usuario radios continuamente con input() hasta que ingrese 'salir', calculando el área de cada radio válido o pidiendo el dato de nuevo si no es válido.
"""

# importing the math module
import math

# --- PART 1: Iteration through a list of data (FOR Loop) ---

radii = [5, 12, -3, 8, 0]

print("--- Processing list of radii ---")

for radius in radii:

    # Check with if/else if the radius is valid (greater than 0).
    if radius > 0:
        area = math.pi * (radius ** 2)
        print(f"Radius: {radius} -> Area: {area:.2f}")
    else:
        print(f"Radius: {radius} -> Error: The radius must be greater than zero.")


# --- PART 2: Interactive and continuous iteration (WHILE Loop) ---

print("\n--- Interactive Mode (Type 'exit' to finish) ---")

# Ask the user for radii continuously.
# The loop repeats until the user types 'exit'.

while True:

    user_input = input("Enter the radius of the circle or type 'exit': ")

    if user_input.lower() == "exit":
        print("Program finished.")
        break

    try:
        user_radius = float(user_input)

        if user_radius > 0:
            area = math.pi * (user_radius ** 2)
            print(f"The area of the circle is: {area:.2f}\n")
        else:
            print("Error: The radius must be greater than zero.\n")

    except ValueError:
        print("Error: Please enter a valid number or the word 'exit'.\n")