# ==========================================
#  M5 Proyecto: Pensamiento Algorítmico
#  Christian Mendoza  
#  Fecha: 2026-09-29
# ==========================================

"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""

# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("Bienvenido al programa de comidas de Latinoamérica.")

# TODO #2:
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
print("Puedes escoger entre las siguientes opciones: tacos, ceviche, bandeja paisa, Feijoada y Asado")

# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
comida = input("Cual es el platillo que quieres conocer de donde es originario? ")
# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.
comida = comida.lower()

# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
if comida == "tacos":
    print("Los tacos son un platillo originario de México.")
elif comida == "ceviche":
    print("El ceviche es un platillo originario de Perú.")
elif comida == "bandeja paisa":
    print("La bandeja paisa es un platillo originario de Colombia.")
elif comida == "feijoada":
    print("La feijoada es un platillo originario de Brasil.")
elif comida == "asado":
    print("El asado es un platillo originario de Argentina.")
else:
    print("Lo siento, no tengo información sobre ese platillo. ")

#Busque los platillos tipicos latinoamericanos en google 

## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""