#grecia lopez orozco
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""

# 1. Pedir la edad al usuario
edad_texto = input("Cual es tu edad?: ")
edad = int(edad_texto)

# 2. Pedir si aprobó el examen de manejo
paso_examen = input("Aprobaste el examen de conducir? (si/no): ").strip().lower()

# 3. Estructura condicional
# Primera sentencia: Debe ser mayor o igual a 18 años y haber pasado el examen
if edad >= 18 and paso_examen == "si":
    print("Felicidades! Eres elegible para tramitar y recibir tu licencia de conducir.")

# Segunda sentencia: Es mayor de edad pero NO aprobó el examen
elif edad >= 18 and paso_examen != "si":
    print("Tienes la edad suficiente, pero debes aprobar el examen práctico/teórico para obtener la licencia.")

# Tercera sentencia: Es menor de edad
else:
    print("Lo sentimos, debes tener 18 años para solicitar la licencia de conducir.")


# respuesta 1: hice 2 commits en total mientras iba haciendo la tarea

#respuesta 2: a mi me gusto mas usar los comandos en la terminal, 
# al principoo da un poquito de miedo pero cuando le agarras el modo a
#  escribir git add o git comit y git push, sientes que tienes mas control 
# de lo que estas haciendo 

#respuesta 3: sirve para revisar como esta todo antes de moverlo, tambien
#  te avisa que archivos cambiastes y cuales todavia no se han aguerdado 
# para que no se te olvide nada antes de hacer el commit

#respuesta 4: porque si la maestra sube algo nuevo o cmbia alguna instroccion, 
# necesitamos tener eso actualizado en nuestra laptop, si no lo hacemos, se puede 
# cruzar las cosas y borrar alguna tare por accidente 

#respuesta 5: fork es como sacarle copia al proyecto de alguine para tenerlo guardado 
# en tu perfil de github y clone es descargar esa copia desde github a tu laptop para 
# poder abrirla en vc code y poder editarla

# respuesta 6: porque si pones nombres claros es facil saber que hicistes en cada paso, 
# pero si solo pones cambios luego ya ni te acuerdas de que era o que es lo que hay ahi  

# respuesta 7: "Agregando el codigo para la tarea de licencia de conducir" 
# "Agregando la condicion de los lentes y la sentencia else"

#respuesta 8: me guto mucho la setence 
# if edad >= 18 and paso_examen == "si" and trae_lentes == "si": 
# porque usa tres condiciones juntas con el operador and para asegurarse 
# de que todo este en orden 

#respuesta 9: entra cuando se cumple que es mayor de edad, pero no cumple la 
# segunda condición que pide el programa para dejarlo manejar

# respuesta 10: aprendi como hacer la tarea del modulo y usar los comentarios 
# con # en python para explicar paso a paso lo que hace mi codigo, ademas de repasar 
# los comandos de git para subir las entregas 