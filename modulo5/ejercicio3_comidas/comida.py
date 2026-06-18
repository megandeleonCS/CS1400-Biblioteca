"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""

# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print('Bienvenidos al programa de comidas de latinoamerica')
# TODO #2:
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
print('Comidas: \n1. Pollo a la brasa\n2. Tacos al pastor\n3. Pozole\n4. Hamburguesa\n5. Pasta')
# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
comida = input('Escribe que comida quieres: ')
# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.
comida = comida.lower()
# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
if comida == 'pollo a la brasa':
    print('Esta comida es de Peru')
    
elif comida == 'tacos al pastor':
    print('Esta comida es de Mexico')

elif comida == 'Pozole':
    print('Esta comida es de Mexico')

elif comida == 'hamburguesa':
    print('Esta comida es de USA')

elif comida == 'pasta':
    print('Esta comida es de Francia')

else:
    print('Esta comida no esta disponible o usaste el numero en vez del nombre de la comida')

## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
