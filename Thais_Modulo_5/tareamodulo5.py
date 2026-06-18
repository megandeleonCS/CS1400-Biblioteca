#Funciones Predefinidas
#Observa el segmento de código a continuación y luego responde las preguntas.

#El siguiente programa tiene como objetivo indicar el número de dígitos que ingresas, o mostrar un valor negativo si tienes un número negativo.

#Python
#librería math en python
import math
from turtle import distance

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Pregunta 1
print( round(decNum, 0) )   # Pregunta 2
print( int(decNum))         # Pregunta 3
print( abs(decNum) )        # Pregunta 4

print( math.pow(intNum, 2) )     # Pregunta 5
print( math.sqrt(intNum) )       # Pregunta 6
#Predicciones de salida:
#1. ¿Resultado del primer print? -34.57 porque la funcion redondea a dos decimales
#2. ¿Resultado del segundo print? -35.0 la funcion redondea los decimales a 0
#3. ¿Resultado del tercer print? -34 int() no redondea, solo eliminda los decimales
#4. ¿Resultado del cuarto print?  la funcion abs() devuelve el valor absolute, es decir sin signo negativo
#5. ¿Resultado del quinto print? 81.0 porque la funcion  math.pow(9,2) calcula 9 al cuadrado y devuelve un float
#6. ¿Resultado del sexto print? 3.0 porque la raíz cuadrada de 9 es 3 math.sqrt() devuelve un float.
#Máximo y Mínimo (Max and Min)
#Observa la función max() en el segmento de código de abajo.

mimax = max("manzana", "Banano", "Zanahoria")
print(mimax)

#7. ¿Cuál crees que será el resultado al comparar "manzana", "Banana" y "Zanahoria"? 
#Respuesta: "manzana"  porque Python ordena las cadenas alfabeticamente y distingue mayusculas. Las palabras con minuscula son leidas despues de las palabras que empiezan con mayusculas

#8. Ejecuta el código, ¿fue correcta tu suposición? 
#Respuesta:Si, porque al ejecutar el codigo se obtiene exactamente manzana

#9. Si cambias "manzana" por "Manzana" (mayúscula), ¿crees que esto cambiará el resultado? 
#Respuesta: Si cambia ahora el resultado es Zanahoria. Porque Manzana empieza con mayuscula y queda antes del orden alfabetico, por lo que zanahoria pasa a ser el mayor

#10. Cambia la llamada de la función max por min. ¿Obtienes el valor más pequeño? 
#Respuesta: Si, Banana. Porque  min() devuelve el primer valor en el orden alfabetico, las mayusculas se ordenan antes.

#Funciones Matemáticas
#La policía necesita una aplicación para determinar la velocidad de los autos en un choque mediante la longitud de las huellas de frenado d. La ecuación es:
#v = math.sqrt(30 * d) 
#Esta formula require multiplicar la distancia por 30 y luego sacar la raíz cuadrada.

#Instrucciones:

#11. Completa el código a continuación para calcular la velocidad y redondear la respuesta a 2 decimales.

#Velocidad del auto
import math

#d = longitud de la huella de frenado (distancia)
d = float (input("Ingresa la longitud de la huella de freanado:  "))
if d < 0:
  print ('Error: la distancia no puede ser negativa. "')
else:
  v = math.sqrt(30 * d)
  print("velocidad del auto: ", round(v, 2))                

# 12. Escribe la ecuación aquí:
v = math.sqrt(30 * d)
print("Velocidad del auto:", round(v, 2))
 
#d es la distancia de la huella de frenado, y round redondea a dos decimales
#Cadenas de Texto (Strings)

#Observa los segmentos de código. Responde las preguntas realizando predicciones, observaciones y ejecutando el código.

#13. Observa las variables sujeto1 y sujeto2. ¿Cuál es la diferencia entre los textos? Los textos son diferentes. El sujeto = "Python" en mayuscula y el sujeto2 = "python" en minuscula

#14. Ejecuta el código, ¿los valores se comparan como iguales o diferentes? 
#Respuesta: Iguales porque ambos quedan como python, en minuscula (las minusculas se leen primero)

sujeto1 = "Python"
sujeto2 = "python"

if sujeto1 == sujeto2:
  print("Iguales")
else:
  print("Diferentes")

#15. Una forma de hacer que la comparación no distinga entre mayúsculas y minúsculas es convertir todos los caracteres al mismo formato. Agrega .lower() al final de sujeto1 y sujeto2 en la sentencia if.

#16. Ejecuta el programa de nuevo, ¿los valores son iguales o diferentes? 

if sujeto1 == sujeto2:
  print("Iguales")
else:
  print("Diferentes")
#Segmentación de Cadenas (Slicing)

nombre = "Building Puentes"
print(nombre[0])
print(nombre[8 : 10])

#17. ¿Qué letra imprime exactamente nombre[0]? 
#Respuesta es"B" porque el indice 0 siempre corresponde al primer caracter.

#18. ¿En qué posición (índice) está el primer espacio en "Building Puentes"?
#Respuesta: en el 8. Por que los indices comienzan en el cero y el espacio Comienza despues de Building contando el espacio.

#19. Corrige nombre[X : Y] para que imprima exactamente "Puentes". 
#Respuesta: nombre[9:16] porque Puentes comienzan en el espacio 9 y termina antes del 16.


#Iteración de Cadenas
#Observa los dos segmentos de código y responde:

str_val = "hello"
for i in range(0, 5):
  print (str_val[i])

#20. ¿Cuál es la longitud de la cadena str_val? 
#Respuesta: la longitude de "hello" es 5 porque tiene 5 caracteres

#21. Observa el rango (range) del ciclo for. ¿Por qué crees que usa el rango 0, 5? 
#Respuesta: porque los indices van de 0 a 4, Python Comienza a contar desde 0

#22. Observa el print. ¿Qué valor de la cadena se está imprimiendo?
#Respuesta: imprime un caracter del string porque accede a la letra desde la posicion i 

#23. ¿Qué crees que se imprimirá al ejecutar el código? Ejecútalo para verificarlo.
#Respuesta, imprime todas las letras de hello, recorre todas las posiciones del string.

#Modifica la variable str_val para que, en lugar de ser la palabra "hello", use un input que permita al usuario ingresar cualquier palabra.

#24. Ejecuta el programa e ingresa una palabra muy larga. ¿Se imprimió la palabra completa? 
#Respuesta: No porque el rango indica que debe abarcar solo cinco caracteres

#Nota el rango del ciclo de nuevo, solo llega hasta 5. La función len nos permite hacer que el rango llegue hasta la longitud de la palabra. Reemplaza el 5 con len(str_val).

#25. Ejecuta el programa de nuevo e ingresa una palabra larga. ¿Se imprimió completa esta vez? 
#Respuestas: Si se imprimio.

#26. El último carácter siempre está una posición por debajo de la longitud (si la longitud es 5, la última posición es 4). Queremos modificar el ciclo para que muestre la #palabra en orden inverso. ¿Qué podrías restar a la longitud para que empiece en la posición correcta? 
#Respuesta: 1 porque el ultimo indice siempre es len-1

#Modifica el resto de los valores en el range para que la palabra se muestre en orden inverso, un carácter por línea.

#Ahora mira este código y compáralo con el anterior:

str_val = "hello"
for i in str_val:
  print (i)

#27. ¿Cuál es la diferencia entre cómo se comportan y cómo están programados? 
#Respuesta: uno recorre indice y el otro letras

texto = input("Ingresa una frase que contenga texto y números: ")
for i in range(0, len(texto)):
  if texto[i] >= "0" and texto[i] <= "9":
    print("Hay un número en la posición: ", i)

#28. Ejecuta el programa. Ingresa una frase con números (ej. 3 tigres). ¿El programa reporta las posiciones correctamente?
#Respuesta: Si las reporta porque identifica los caracteres numericos. Porque cada vez que el programa encuentra un dígito, imprime el índice `i`, que corresponde a la posición exacta del carácter dentro del texto.


#29. Observa el if. ¿Con qué se compara cada carácter para determinar si es un valor numérico?
#Respuesta: Con `"0"` y `"9"`.
#Porque en ASCII/Unicode los dígitos están ordenados consecutivamente, y cualquier carácter entre `"0"` y `"9"` corresponde a un número.


texto = input("Ingresa una frase que contenga texto y números: ")

#inicializar el contador
numeros = 0

# recorrer el texto carácter por carácter
for i in range(0, len(texto)):
  if texto[i] >= "0" and texto[i] <= "9":
    numeros += 1

# mostrar el total de números encontrados
print("Total de números:", numeros)

#Porque, en lugar de imprimir cada posición donde aparece un número, el contador `numeros` se incrementa en 1 cada vez que se encuentra un dígito, permitiendo obtener el #total al final del ciclo.


