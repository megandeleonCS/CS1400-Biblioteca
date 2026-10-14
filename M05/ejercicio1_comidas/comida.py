"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""
#He empezado a trabajar en el programa y voy a publicar el mensaje de bienvenida.
# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("bienvenido al programa de comidas de Latinoamérica")
# TODO #2:
# Aquí estoy preparando el menú.
# Muestra al usuario una lista de al menos 5 opciones de comida para elegir..
print(" menu")
print("galinhada $10")
print("feijoada $20")
print("lasanha $30")
print("churrasco $40")
print("PF de posto $50")
# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
#usando lower para q nao haja divergencia na variavel.
# Aqui estou dando a opcao de escolha ao cliente.
comida = input("¿Qué comida te gustaría?\n").lower()
#
# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.

# TODO #5:
# Usa una  if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
#Estoy utilizando variables para que el cliente reciba un mensaje según su elección.
if comida == "galinhada":
    print ("Un delicioso estofado de pollo en camino..")
elif comida == "feijoada":
    print("esto es muy bueno.")
elif comida == "lasanha":
    print(" Este plato es maravilloso.")
elif comida == "churrasco":
    print("Este es auténticamente brasileño..")
elif comida == "PF de posto":
    print("esto es muy barato.")
else:
    print("Te daré unos minutos más para que decidas..")
    
## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
