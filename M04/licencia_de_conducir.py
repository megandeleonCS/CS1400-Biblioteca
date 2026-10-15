#CHRISTIAN MENDOZA
#22 SEPTIEMBRE 2026
#M4 TAREA PRESENCIAL 2 DE 2

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
print("Evaluación de condiciones para conducir")

# ENTRADA DE DATOS
edad = int(input("Ingresa tu edad: "))

# VERIFICACION DE LA EDAD
if edad < 18:
    print("No puedes conducir por que aun eres menor de edad. Vuelve en un año")
#SI SI ES MAYOR DE 18, PASA A LAS SIGUIENTES PREGUNTAS
else:
    print("Responde las siguientes preguntas, para completar la solicitud.")
  
    # PREGUNTAS PARA CONTINUAR
    tiene_licencia = input("¿Tienes licencia vigente? (s/n): ").strip().lower() == "s"
    alcohol = input("¿Has consumido alcohol recientemente? (s/n): ").strip().lower() == "s"
    cansado = input("¿Te sientes cansado o somnoliento? (s/n): ").strip().lower() == "s"

  #ESTRUCTURA DE CONTROL PARA EVALUAR CONDICIONES

  #CASO 1 ESTA ALCOHOLIZADO O CANSADO
    if alcohol or cansado:
      print("No puedes conducir debido a tus condiciones actuales. Entrega las llaves inmediatamente.")
  #CASO 2 NO TIENE LICENCIA VIGENTE
    elif not tiene_licencia:
      print("No puedes conducir porque no tienes una licencia vigente, tramita una.")
  #CASO 3 TIENE LICENCIA, NO ESTA ALCOHOLIZADO NI CANSADO
    elif tiene_licencia and not alcohol and not cansado:
      print("Puedes conducir. Cumples con todos los requisitos! Ve por tu licencia y que Diosito te bendiga!")

    else:
      print("No se puede completar la evaluación.")


"""
1. ¿Cuántos commits hiciste?
Creo que 3 o 4 cuando sentia que era un cambio "grande".
2. ¿Qué método te pareció más fácil de usar para guardar y subir tus cambios a GitHub: los comandos en la terminal o la interfaz visual de Visual Studio Code? ¿Por qué?
La interfaz de VSC por que es mas "intuitivo" por asi decirlo, con solo pocos clics te permite guardar y subir los cambios.
3. ¿Para qué sirve ejecutar el comando git status antes de empezar a trabajar y cómo te ayuda a saber qué archivos han sido modificados o están pendientes por guardar?
Para ver si hubo cambios en los archivos, para ver si te falta algo por guardar/subir y asi asegurarte de que todo esta actualizado.
4. ¿Por qué es fundamental descargar (git pull) los cambios más recientes del repositorio de la profesora antes de realizar y subir tus propias modificaciones al proyecto?
POr que con esto te aseguras de estar trabajando/modificando la version actual de la profesora, por si hubo algun cambio desde la ultima vez que lo abriste.
5. En tus propias palabras, ¿cuál es la diferencia entre hacer un fork de un repositorio en GitHub y clonar (clone) un repositorio a tu computadora?
Que el fork es como una copia en tu cuenta de github, para asi poderle hacer cambios sin afectar el repositorio original. y el clonar se guarda en tu computadora local y ahi si las modificaciones afectan la copia local. 
6. ¿Por qué es una buena práctica escribir mensajes claros y descriptivos en cada commit (por ejemplo: "Agregando mi nombre al proyecto de M4") en lugar de usar palabras vagas como "cambios" o "listo"?
Por que con ellos te puedes dar cuenta exactamente del cambio que realizaste y el motivo del mismo.
7. ¿Qué tipos de mensajes agregaste?
Agregue mensajes mencionando los cambios "Grandes" que habia realizado en cada commit.
8. ¿Cuál es tu sentencia preferida?
Mi sentencia preferida es en el CASO 3 por que cumple con todos los requisitos y mandas al usuario a sacar su licencia con la bendicion de Dios.
9. ¿Cuándo entra el programa a la segunda sentencia de tu tarea?
Entra a la segunda sentencia en el elif not tiene_licencia.
10. ¿Qué aprendiste del README.md en tu carpeta M04? No olvides los comentarios!
Aprendi el uso de github y como conectarlo directamente a mi VS Code.


"""