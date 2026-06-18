#1.Imprime un mensaje de bienvenida al grupo de comidas de Latinoamerica.
print("Bienvenido al programa de comidas de Latinoamerica ")

#2.Muestra al usuario una lista de al menos 5 opciones de comidas para eligir
print("opciones: Arroz, Asado, Ceviche, Pupusa, Arepa")

#3.Guarda lo que el usuario escribio en una variable llamada  "comida"
comida = input("¿Que comida quieres conocer?")

#4.Convierte lo ingresado a minusculas para asegurar la comparacion correcta
comida = comida.lower ()

#5.Usa una estructura if/elif/else para verificar la comida elegida
#imprime un mensaje con el pais de origen para cada comida

if comida == "arroz":
    print("El arroz es tipico de Colombia.")
elif comida == "asado":
    print("El asado es tipico de Argentina.")
elif comida == "ceviche":
    print("El ceviche es tipico de Peru.")
elif comida == "pupusa":
    print("La pupusa es tipico de el Salvador")
elif comida == "arepa":
    print("La arepa son tipicas de Venezuela")
