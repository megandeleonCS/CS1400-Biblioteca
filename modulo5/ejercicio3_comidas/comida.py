"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""
# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("Bienvenido al programa de comidas de latinoamerica")

# TODO #2:
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
menu = ["tacos", "arepas", "ceviche", "pupusas", "asado" ]
print(menu)

# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
comida = input("¿Que comida quieres comer? ")

# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.
resultado = comida.lower()

# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
if resultado == "tacos":
    print("Los tacos son tipicos de Mexico")
elif resultado == "arepas":
    print("Las arepas son tipicas de Colombia")
elif resultado == "ceviche":
    print("El ceviche es tipico de Peru")
elif resultado == "pupusas":
    print("Las pupusas son tipicas del Salvador")
elif resultado == "asado":
    print("El asado es tipico de Argentina")
else:
    print("Eso no esta en el menu")

## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""