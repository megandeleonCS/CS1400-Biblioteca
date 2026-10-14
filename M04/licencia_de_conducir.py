#Marco
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
#
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
 #
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
 #
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""
# iniciando el programa de rutina dz.
print("¡Buenas tardes! Bienvenido al DMV.")
print("Este es un procedimiento de rutina.")
edad = int(input("¿Cuántos años tienes?"))
if edad < 18:
    print("Vete a casa y espera a cumplir la mayoría de edad. Es necesario tener 18 años o más para poder conducir..")
#añadiendo el else para continuar el programa en caso de que la persona sea mayor de 18 años.
else:

  print("Dame tu licencia de conducir.")
  seguridad = input("¿Lleva puesto el cinturón de seguridad? (si/no)").lower()
  sueño = input("¿Durmió menos de 4 horas esta noche? (si/no)").lower()
  gafas = input("¿Olvidaste tus gafas? ¿Te peleaste con ellas, o qué? (si/no)").lower()
#añadiendo las condicionales.
  if seguridad == "si" and sueño == "no" and gafas == "no":
     print("Puede continuar su viaje.")
  elif gafas == "si" or sueño == "si":
    print("entrega las llaves.")
  elif not seguridad == "si":
     print("Ponte el cinturón antes de salir..")
  else:
     print("Pide un Uber.")
  